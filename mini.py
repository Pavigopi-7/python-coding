from fastapi import FastAPI HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()
class Note(BaseModel):
    id:int
    title:str
    content:str
fake_notes_db: List[Note] = []
@app.post("/notes/")
def create(note:Note):
    fake_notes_db.append(note)
    return{
        "message":"Notes Added Successfully",
        "Note": note
    }
@app.get("/notes/")
def get_notes():
    return fake_notes_db

@app.put("/notes/{note_id}")
def update(note_id:int,updated_note:Note):
    for index, note in enumerate(fake_notes_db):
    if note.id == note_id:
        fake_notes_db[index] = updated_note
        return{"message":"Note updated successfully",
        "Note":updated_note
        }
    raise HTTPException(status_code=404, detail="Note not found")

@app.delete("/notes/{note_id}")
def delete(note_id:int):
    for index, note in enumerate(fake_notes_db):
    if note.id == note_id:
    del fake_notes_db[index]
    return {"message": "Note deleted successfully"}
raise HTTPException(status_code=404, detail="Note not found")
    
@app.get("/notes/search/")
def search(title: Optional[str] = None):
    if not title:
        return fake_notes_db
    result = [note for note in fake_notes_db if title.lower() in note.title.lower()]
    if not result:
        return {"message": "No matching notes found"}
        return result