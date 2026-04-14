from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def create_vector_store(chunks):
    """Create a FAISS vector store from document chunks."""

    # Embedding model to convert text into vectors
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Build FAISS index from chunks
    vectorstore = FAISS.from_documents(chunks, embeddings)

    return vectorstore
