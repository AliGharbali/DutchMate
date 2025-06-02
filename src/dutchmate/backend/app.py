import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4.1"

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found in environment. Please set it in your .env file.")

openai.api_key = OPENAI_API_KEY

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

def call_gpt41(prompt: str, system: str = "You are a helpful Dutch B1 tutor.") -> str:
    try:
        response = openai.ChatCompletion.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=512
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error calling OpenAI: {e}"

@app.post("/start-lesson/")
def start_lesson(request: LessonRequest):
    # Placeholder: fetch lesson template and resources
    return {"message": f"Lesson {request.lesson_id} started.", "lesson": {}}

@app.post("/submit-answer/")
def submit_answer(submission: AnswerSubmission):
    # Example: Use GPT-4.1 to score/feedback (placeholder prompt)
    prompt = f"Evaluate this {submission.skill} answer for a Dutch B1 learner: {submission.answer}"
    feedback = call_gpt41(prompt)
    return {
        "message": f"Answer for lesson {submission.lesson_id}, skill {submission.skill} received.",
        "score": None,
        "feedback": feedback
    }

@app.post("/review/")
def review(request: ReviewRequest):
    # Placeholder: fetch review/rehearsal items for user
    return {"message": "Review session started.", "items": []}
