from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from parser import extract_text
from prompts import build_prompt
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Study Notes Tool",
    description="Upload a PDF and get summary, flashcards, key terms, and quiz questions.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate")
async def generate_notes(file: UploadFile = File(...)):
    file_bytes = await file.read()
    text = extract_text(file_bytes)

    if not text.strip():
        return {"error": "No text could be extracted from the PDF."}

    prompt = build_prompt(text)

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    content = response.choices[0].message["content"]
    return {"notes": content}
