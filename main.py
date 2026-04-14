from app.ingestion.loader import load_document
from app.ingestion.chunker import split_documents
from app.retrieval.vector_store import create_vector_store
from app.retrieval.retriever import get_retriever
from app.generation.rag_pipeline import run_rag

docs = load_document("data/sample.txt")
chunks = split_documents(docs)

vectorstore = create_vector_store(chunks)
retriever = get_retriever(vectorstore)

query = input("Ask something: ")
answer = run_rag(query, retriever)

print("\nAnswer:\n", answer)
