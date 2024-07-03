from fastapi import FastAPI
from app.routers import docs

# Initialize the FastAPI application
app = FastAPI(title='Zania-RAG-Langchain-OpenAI')

# Include the router for document-related endpoints
app.include_router(docs.router)
