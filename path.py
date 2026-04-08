from fastapi import FastAPI

app = FastAPI()

students = {
    "id":01, 
    "Name":"xxx", 
    "Tamil":60,
    "English":88,
}
{
    "id":02,
    "Name":"yyy",
    "Tamil":78,
    "English":88
}

@app.get("/student/{student_id}")
def stu(student_id:int):
    if student_id in students:
        return students[student_id]
        else:
            return{"error":"student id no not found"}