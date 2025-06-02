"""
Script: chunk_and_embed.py

This script processes resource files for DutchMate:
- Loads each text resource from backend/resources/
- Splits (chunks) the text into manageable segments (e.g., 200-300 tokens)
- Embeds each chunk using OpenAI embeddings
- Stores the embeddings in a ChromaDB vector database

Usage:
    python scripts/chunk_and_embed.py

Requirements:
    - openai
    - chromadb
"""

import os
from pathlib import Path

# Placeholder imports for actual embedding and vector DB logic
# import openai
# import chromadb

RESOURCE_DIR = Path(__file__).parent.parent / "backend" / "resources"

def chunk_text(text, max_tokens=250):
    # Simple chunking by sentences (placeholder)
    sentences = text.split('. ')
    chunks = []
    current = ""
    for sentence in sentences:
        if len(current) + len(sentence) < max_tokens:
            current += sentence + ". "
        else:
            chunks.append(current.strip())
            current = sentence + ". "
    if current:
        chunks.append(current.strip())
    return chunks

def process_resources():
    for file in RESOURCE_DIR.glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()
        chunks = chunk_text(text)
        print(f"Processing {file.name}: {len(chunks)} chunks")
        # TODO: Embed each chunk and store in ChromaDB

if __name__ == "__main__":
    process_resources()
