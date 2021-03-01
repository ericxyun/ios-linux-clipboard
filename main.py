from typing import Optional, List
from fastapi import FastAPI, Header, Request
from urllib.parse import unquote
import pyperclip 
from tinydb import TinyDB, Query

app = FastAPI()

# local data to read from ios
db = TinyDB('db.json')

@app.get("/")
def read_root():
    return {"clipboard_content": pyperclip.paste()}

@app.get("/clipboard/")
def get_clipboard(content: Optional[str] = Header(None)):
    content = unquote(content)
    pyperclip.copy(content)
    return {
        "message": "Successfully copied",
        "content": content
    }

@app.post("/clipboard/")
def set_clipboard(content: Optional[str] = Header(None)):
    # clipboard_content = content
    # pyperclip.copy(content)
    return {
        "content": pyperclip.paste()
    }
