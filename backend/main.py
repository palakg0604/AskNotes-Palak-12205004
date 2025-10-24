from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from backend.parse_utils import extract_text
from backend.ai_client import summarize_text, generate_quiz

app = FastAPI(title="AskNotes API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("./uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text(str(file_path), file.filename)
    if not text.strip():
        raise HTTPException(status_code=400, detail="No text extracted.")

    summary = summarize_text(text)
    quiz = generate_quiz(text)
    return {"filename": file.filename, "summary": summary, "quiz": quiz}
