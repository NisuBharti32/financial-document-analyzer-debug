from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
import asyncio

from crewai import Crew, Process
from agents import (
    financial_analyst as financial_analyst_agent,
    investment_advisor as investment_advisor_agent,
    risk_assessor as risk_assessor_agent,
    verifier as verifier_agent
)
from task import (
    analyze_financial_document as analyze_task,
    investment_analysis as investment_task,
    risk_assessment as risk_task,
    verification as verification_task
)

app = FastAPI(title="Financial Document Analyzer")

def run_crew(query: str, file_path: str):
    """To run the whole crew"""
    financial_crew = Crew(
        agents=[verifier_agent, financial_analyst_agent, investment_advisor_agent, risk_assessor_agent],
        tasks=[verification_task, analyze_task, investment_task, risk_task],
        process=Process.sequential,
    )
    
    # Pass path as well so it's available for tasks/tools
    result = financial_crew.kickoff(inputs={'query': query, 'path': file_path})
    return result

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Financial Document Analyzer API is running"}

@app.post("/analyze")
async def analyze_document_endpoint(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    """Analyze financial document and provide comprehensive investment recommendations"""
    
    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"
    
    try:
        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)
        
        # Save uploaded file
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Validate query
        if query=="" or query is None:
            query = "Analyze this financial document for investment insights"
            
        # Process the financial document with all analysts
        response = run_crew(query=query.strip(), file_path=file_path)
        
        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing financial document: {str(e)}")
    
    finally:
        # Clean up uploaded file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass  # Ignore cleanup errors

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)