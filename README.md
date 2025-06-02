# DutchMate

DutchMate is an interactive, AI-powered Dutch language tutor designed to help learners reach CEFR B1 proficiency. It leverages state-of-the-art language models (LLMs) and a small curated set of real B1-level resources to deliver engaging lessons, adaptive practice, and automated assessment across all four language skills: reading, listening, speaking, and writing.

## Features

- **10-lesson syllabus** covering B1 grammar, vocabulary, and real-life themes
- **Interactive activities** for reading, listening, speaking, and writing
- **Automated scoring** and feedback using LLMs and clear rubrics
- **Adaptive rehearsal**: personalized review based on your progress and mistakes
- **Retrieval-Augmented Generation (RAG)**: combines LLM knowledge with authentic B1 resources
- **Progress tracking** and analytics

## Project Structure

```
backend/         # LLM, RAG, scoring, analytics
  app.py
  lessons/       # Lesson templates and rubrics
  resources/     # Processed B1 resources (chunked, embedded)
  db/            # User state, scores, analytics

frontend/        # UI (Streamlit or React)
  ...

data/            # Downloaded B1 resources (texts, audio, etc.)

scripts/         # Utilities for scraping, chunking, embedding

README.md
requirements.txt
```

## Installation

1. Install dependencies with [uv](https://github.com/astral-sh/uv):
   ```
   uv sync
   ```

2. Create a `.env` file in your project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-...
   ```

3. Run the backend:
   ```
   uvicorn dutchmate.backend.app:app --reload --app-dir src
   ```

4. Run the frontend:
   ```
   streamlit run src/dutchmate/frontend/app.py
   ```

5. Download or copy B1-level Dutch resources (texts, audio, transcripts) into `src/dutchmate/resources/`.

## License

MIT License
