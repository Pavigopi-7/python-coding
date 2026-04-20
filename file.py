from fastapi import FastAPI, UploadFile,File
from fastapi.responses import JSONResponse
app = FastAPI()
@app.POST("/upload/")
async def upload_file(file: UploadFile = File(note.txt)):
    content = await file.read()
with open(file.note, "wb") as f:
    f.write(content)
 return JSONResponse(content={
        "note file": file.note,
        "content_type": file.content_type,
        "message": "File uploaded successfully"
    })