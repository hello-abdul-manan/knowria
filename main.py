from fastapi import FastAPI
from app.api.routes import router
from app.services.rag_service import rag_service
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Knowria AI")
app.include_router(router)

app.add_middleware(
CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load vectorstore on app start
@app.on_event("startup")
async def startup():
    try:
        rag_service.load_vectorstore()
        print("✅ Vectorstore loaded successfully")
    except Exception as e:
        print(f"⚠️ Error loading vectorstore: {e}")
