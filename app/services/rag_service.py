import os
from app.ingestion.loader import load_document
from app.ingestion.chunker import split_documents
from app.retrieval.vector_store import create_vector_store
from app.retrieval.retriever import get_retriever
from app.generation.rag_pipeline import run_rag
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Path to save vector store
VECTOR_PATH = "data/vectorstore"

class RAGService:
    """Handles document ingestion, vector store and querying."""

    def __init__(self):
        """Initialize with empty vector store and retriever."""
        self.vectorstore = None
        self.retriever = None

    def ingest(self, file_path: str):
        """Ingest a document, create a vector store."""
        # Load and split document
        docs = load_document(file_path)
        chunks = split_documents(docs)

        # Create and save vector store locally
        self.vectorstore = create_vector_store(chunks)
        self.vectorstore.save_local(VECTOR_PATH)

        self.retriever = get_retriever(self.vectorstore)

    def load_vectorstore(self):
        """Load vector store and retriever from local storage."""

        # Use HuggingFace embedding model
        embeddings = HuggingFaceEmbeddings(
            model_name = "sentence-transformers/all-MiniLM-L6-v2"
        )

        # Load if exists
        if os.path.exists(VECTOR_PATH):
            self.vectorstore = FAISS.load_local(
                VECTOR_PATH, embeddings, allow_dangerous_deserialization=True
            )
            self.retriever = get_retriever(self.vectorstore)

    def query(self, question: str):
        """Query the retriever for an answer."""

        if not self.retriever:
            return "No documents uploaded yet."

        # Get answer using RAG pipeline
        return run_rag(question, self.retriever)

# Instantiate RAG service
rag_service = RAGService()
