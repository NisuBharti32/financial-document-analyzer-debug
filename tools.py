## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import tool
from langchain_community.document_loaders import PyPDFLoader
from crewai_tools import SerperDevTool

## Creating search tool
search_tool = SerperDevTool()

@tool("read_data_tool")
def read_data_tool(path: str = None, **kwargs):
    """Tool to read data from a pdf file from a path.
    Args:
        path (str): The path to the PDF file.
    """
    # CrewAI sometimes passes the input as a string directly, 
    # or as a dictionary within kwargs, or as the first positional argument.
    
    file_path = path
    if not file_path and 'path' in kwargs:
        file_path = kwargs['path']
    if not file_path and kwargs:
        # If still not found, try to get the first value from kwargs
        file_path = next(iter(kwargs.values()), None)

    if not file_path:
        return "Error: No path provided to the tool. Please provide the 'path' to the PDF file."

    if not os.path.exists(file_path):
        return f"Error: File not found at {file_path}"
    
    try:
        # Use file_path instead of path
        print(f"DEBUG: Loading PDF from {file_path}")
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        
        if not docs:
            print("DEBUG: No documents loaded from PDF")
            return "Error: PDF file is empty or could not be parsed."

        full_report = ""
        for data in docs:
            content = data.page_content
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"
        
        print(f"DEBUG: Successfully read {len(full_report)} characters from PDF")
        return full_report
    except Exception as e:
        print(f"DEBUG: Exception in read_data_tool: {str(e)}")
        import traceback
        traceback.print_exc()
        return f"Error reading PDF: {str(e)}"

@tool("analyze_investment_tool")
def analyze_investment_tool(financial_document_data: str):
    """Tool to analyze investment potential from financial data."""
    # For now, return a placeholder or implement basic logic
    return f"Analyzing investment data: {financial_document_data[:100]}..."

@tool("create_risk_assessment_tool")
def create_risk_assessment_tool(financial_document_data: str):
    """Tool to assess risks from financial data."""
    return f"Assessing risks for data: {financial_document_data[:100]}..."