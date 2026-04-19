from fastapi import APIRouter, UploadFile, File
import os
from app.services.rag_service import rag_service

router = APIRouter()

# Directory for file uploads
UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# POST endpoint to upload and process file
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save the uploaded file
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Ingest the file for processing
    rag_service.ingest(file_path)

    return {"message": "File uploaded and processed successfully"}

# GET endpoint to query the uploaded files
@router.get("/query")
def query(question: str):
    answer = rag_service.query(question)
    return {"answer": answer}
