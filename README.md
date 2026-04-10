# AI Document Summarization Service

An AI-powered document summarization application built using Python, Streamlit, and Google Gemini.
It transforms raw text or uploaded documents into structured, high-quality summaries with clarity and consistency.

# Overview

This project demonstrates a production-oriented implementation of an LLM-based summarization system.
It focuses on reliability, scalability, and clean architecture, while handling real-world constraints like token limits and API stability.

The application supports multiple summarization styles and ensures meaningful, well-structured outputs even for large documents.

# Features

* Summarization of PDF, TXT, and DOCX documents
* AI-powered summaries using Google Gemini (LLM)
* Multiple output styles:
 *  Brief summary
 *  Bullet-point summary
 *  Detailed summary
* Long-form notes (1500+ words)
* Chunking + multi-stage summarization for large documents
* Environment-based configuration (secure API handling)
* Clean and interactive Streamlit UI
* Downloadable summaries


# Tech Stack
Layer	Technology
Language	Python 3
LLM	Google Gemini (google-genai)
Frontend	Streamlit
Config	python-dotenv
Deployment	Local / Cloud-ready

# Repository Structure
Document_Summarization/
│
├── app.py               # Streamlit UI
├── summarization.py     # Core summarization logic
├── config.py            # Environment & config handling
├── .env                 # API keys (ignored by git)
└── requirements.txt     # Dependencies

# 🌐 Live Demo

https://document-summarization-service-llm-powered-9lujazvwwgi7jrkeaqr.streamlit.app/

# Setup Instructions

## Clone Repository
git clone <https://github.com/Ashish-Rawat7/Document-Summarization-Service-LLM-Powered>
cd Document_Summarization

## (Optional) Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

## Install Dependencies
pip install -r requirements.txt

## Configure Environment Variables

Create a .env file in the root directory:

GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-1.5-flash


# Restart the terminal after creating the .env file.

## Run the Application
python -m streamlit run app.py

# Design Decisions & Approach

## Token-Safe LLM Usage

Input text is explicitly capped before being sent to Gemini

Output token limits are carefully tuned

Prevents mid-sentence truncation on Gemini free tier

## Content-Based Summarization

Prompts explicitly disallow meta-commentary

Summaries are written as direct factual statements

## Deterministic Output Length

Programmatic enforcement guarantees minimum 3 sentences

Prevents over-compression and one-line summaries

## Separation of Concerns

UI, summarization logic, and configuration are cleanly separated

Improves readability, maintainability, and extensibility

 Known Limitations

Text input only (no PDF/DOCX upload)

Single-document summarization

Gemini Free Tier token constraints

These are intentional design trade-offs to ensure reliability and correctness.