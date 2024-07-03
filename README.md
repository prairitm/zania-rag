# zania-rag
# FastAPI PDF Document Processing and QA Application

This FastAPI application allows users to upload PDF documents, process them using LangChain for document processing, and query the documents using a question-answering system powered by OpenAI's GPT-3.5.

## Features

- Upload PDF documents and process them into a vector store
- Query the processed documents using natural language questions
- Powered by LangChain and OpenAI

## Directory Structure

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/fastapi_app.git
    cd zania-rag
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set environment variables:**
    Create a `.env` file in the `app` directory and add:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. **Run the application:**
    ```bash
    uvicorn app.main:app --reload
    ```

2. **Open your browser and navigate to:**
    ```
    http://127.0.0.1:8000/docs
    ```

3. **Endpoints:**

    - **Upload PDF:**
        ```
        POST /upload/
        ```
        Upload a PDF file to be processed.

    - **Query Documents:**
        ```
        GET /query/
        ```
        Query the processed documents using a natural language question.

## Example

1. **Upload a PDF:**
    ```bash
    curl -X POST "http://127.0.0.1:8000/upload/" -F "file=@path_to_your_pdf.pdf"
    ```

2. **Query the uploaded document:**
    ```bash
    curl -X GET "http://127.0.0.1:8000/query/?question=What is the termination policy?"
    ```

