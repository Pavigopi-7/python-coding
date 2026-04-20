from fastapi import FastAPI HTTPException
from pydantic import BaseModel

class Note(BaseModel):
    id:int
    title:str
    content:str
app = FastAPI()
@app.get("/notes/{id}")
def get_item(id: int):
    if id != 1:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )
    return {"Id": id}