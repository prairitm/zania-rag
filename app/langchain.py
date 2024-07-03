import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set the OpenAI API key from the environment variable
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

def process_pdf(file_path: str):
    """
    Process a PDF file to create a vector store.
    
    Parameters:
    - file_path: The path to the PDF file.
    
    Returns:
    - db: A FAISS vector store created from the PDF documents.
    """
    loader = PyPDFLoader(file_path)  # Load the PDF
    docs = loader.load()  # Extract documents from the PDF
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=0)  # Initialize text splitter
    documents = text_splitter.split_documents(docs)  # Split documents into smaller chunks
    db = FAISS.from_documents(documents, OpenAIEmbeddings())  # Create FAISS vector store with embeddings
    return db

def create_qa_chain(db):
    """
    Create a question-answering chain using the vector store.
    
    Parameters:
    - db: The FAISS vector store.
    
    Returns:
    - qa_chain: A RetrievalQA chain configured for question-answering.
    """
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125")  # Initialize the language model
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=db.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={'score_threshold': 0.7}
        ),
    )
    return qa_chain

def answer_question(db, question: str):
    """
    Answer a question using the QA chain and vector store.
    
    Parameters:
    - db: The FAISS vector store.
    - question: The question to answer.
    
    Returns:
    - result: The answer to the question.
    """
    qa_chain = create_qa_chain(db)  # Create QA chain
    result = qa_chain({"query": question})  # Get the answer to the question
    return result
