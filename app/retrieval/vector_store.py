from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings

def create_vector_store(chunks):
    """Create a FAISS vector store from document chunks."""

    embeddings = FakeEmbeddings(size=384)

    # Build FAISS index from chunks
    vectorstore = FAISS.from_documents(chunks, embeddings)

    return vectorstore
