# Financial Document Analyzer (Debugged Version)

## Overview

This project is a Financial Document Analyzer built using FastAPI and CrewAI.  
It processes uploaded financial PDF documents and performs:

- Financial analysis  
- Investment recommendations  
- Risk assessment  
- Document verification  

This repository contains the debugged and fixed version of the original buggy codebase.

---

## Bugs Identified and Fixed

1. Incorrect Crew task configuration (functions passed instead of Task objects).
2. Invalid tool imports and decorator usage.
3. Model configuration error (`gpt-4-turbo` not accessible).
4. Missing environment variable handling for `OPENAI_API_KEY`.
5. Dependency conflicts between Pydantic v1 and v2.
6. Improper file handling and cleanup in API.
7. Incorrect project structure causing import errors.

All issues were resolved to ensure proper API execution and stable CrewAI workflow.

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd financial-document-analyzer-debug


### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies
```bash
pip install -r requirements.txt

### 4. Create Environment File
Create a .env file in the root directory:
```bash
OPENAI_API_KEY=your_openai_api_key

### 5. Run the application
```bash
uvicorn main:app --port 8001

Open in browser:
```bash
http://127.0.0.1:8001/docs

API Endpoints
GET /
Health check endpoint.
POST /analyze
Upload a financial PDF and provide a query for analysis.

Known Limitation

If the OpenAI API returns a 429 insufficient_quota error, it indicates billing or quota limitations on the API key.
The system works correctly with a valid API key that has available quota.

Tech Stack
FastAPI
CrewAI
LangChain
PyPDFLoader
OpenAI API