from transformers import pipeline
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


class Item(BaseModel):
    original_text: str


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


@app.post("/shorten_text/")
async def shorten_text(item: Item):
    original_text = str(item).replace("  ", " ").strip()
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    short_text = summarizer(original_text, max_length=130, min_length=14, do_sample=False)
    return {"short_text": short_text[0]["summary_text"]}
