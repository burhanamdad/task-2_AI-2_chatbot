# TEYZIX CORE Internal Knowledge Chatbot

## Introduction
A Retrieval-Augmented Generation chatbot for answering employee questions from internal documents.

## Technologies
- Streamlit
- ChromaDB
- SentenceTransformers
- OpenRouter
- Python

## Architecture

PDF
↓
Chunking
↓
Embeddings
↓
ChromaDB
↓
Retriever
↓
LLM
↓
UI

## Setup

pip install -r requirements.txt

streamlit run app.py