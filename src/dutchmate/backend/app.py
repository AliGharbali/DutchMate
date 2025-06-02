from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="DutchMate Backend",
    description="API for DutchMate B1 Dutch language tutor",
    version="0.1.0"
)

class LessonRequest(BaseModel):
    lesson_id: int

class AnswerSubmission(BaseModel):
    lesson_id: int
    skill: str  # reading, listening, speaking, writing
    answer: str
    user_id: Optional[str] = None

class ReviewRequest(BaseModel):
    user_id: Optional[str] = None

@app.post("/start-lesson/")
def start_lesson(request: LessonRequest):
    # Placeholder: fetch lesson template and resources
    return {"message": f"Lesson {request.lesson_id} started.", "lesson": {}}

@app.post("/submit-answer/")
def submit_answer(submission: AnswerSubmission):
    # Placeholder: process answer, score, and store result
    return {"message": f"Answer for lesson {submission.lesson_id}, skill {submission.skill} received.", "score": None, "feedback": ""}

@app.post("/review/")
def review(request: ReviewRequest):
    # Placeholder: fetch review/rehearsal items for user
    return {"message": "Review session started.", "items": []}
