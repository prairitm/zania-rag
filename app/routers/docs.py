from fastapi import APIRouter, UploadFile, File
from app.langchain import process_pdf, answer_question

# Initialize FastAPI router
router = APIRouter()

# Global variable to store the FAISS vector store
db = None

@router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Endpoint to upload a PDF file and process it.
    
    Parameters:
    - file: The PDF file to upload.
    
    Returns:
    - A dictionary with the filename of the uploaded file.
    """
    global db
    file_path = f"app/uploads/{file.filename}"  # Define file path
    # Save the uploaded file to the specified path
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    db = process_pdf(file_path)  # Process the PDF to create the vector store
    return {"response": f'{file.filename} uploaded successfully.'}

@router.get("/query/")
async def query_docs(question: str):
    """
    Endpoint to query the processed documents.
    
    Parameters:
    - question: The question to ask the QA chain.
    
    Returns:
    - The result of the query or an error message if no documents are available.
    """
    global db
    if db is None:
        return {"error": "No document database available. Please upload a PDF first."}
    result = answer_question(db, question)  # Get the answer to the question
    return result
