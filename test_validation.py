
import os
from dotenv import load_dotenv
from crewai import Crew, Process

# Mock/Import from project files
try:
    from agents import financial_analyst, investment_advisor, risk_assessor, verifier
    from task import analyze_financial_document, investment_analysis, risk_assessment, verification
    
    print("Successfully imported agents and tasks.")
    
    # Test Crew instantiation
    crew = Crew(
        agents=[verifier, financial_analyst, investment_advisor, risk_assessor],
        tasks=[verification, analyze_financial_document, investment_analysis, risk_assessment],
        process=Process.sequential
    )
    print("Successfully instantiated Crew.")
    
except Exception as e:
    print(f"Validation failed: {e}")
    import traceback
    traceback.print_exc()
