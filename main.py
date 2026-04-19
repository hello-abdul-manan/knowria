from fastapi import FastAPI
from app.api.routes import router
from app.services.rag_service import rag_service

app = FastAPI(title="Knowria AI")
app.include_router(router)

# Load vectorstore on app start
@app.on_event("startup")
def startup():
    rag_service.load_vectorstore()
