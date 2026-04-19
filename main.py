from app.services.rag_service import RAGService

rag_service = RAGService()
rag_service.ingest('data/sample.txt')
rag_service.load_vectorstore()
response = rag_service.query("What is the leave policy?")
print("Response:", response)