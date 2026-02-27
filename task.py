## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from tools import search_tool, read_data_tool, analyze_investment_tool, create_risk_assessment_tool

# 1. Verification Task
verification = Task(
    description=(
        "Verify that the document at {path} is a valid financial report and contains the necessary data for analysis."
    ),
    expected_output=(
        "A verification report confirming the document's type and its suitability for financial analysis."
    ),
    agent=verifier,
    tools=[read_data_tool],
)

# 2. Analysis Task
analyze_financial_document = Task(
    description=(
        "Analyze the financial document at {path} to address the user's query: {query}. "
        "Focus on extracting relevant financial data, identifying trends, and providing a factual summary strictly based on the document content."
    ),
    expected_output=(
        "A detailed financial analysis report addressing the query with data-backed insights and key performance metrics."
    ),
    agent=financial_analyst,
    tools=[read_data_tool],
)

# 3. Investment Analysis Task
investment_analysis = Task(
    description=(
        "Based on the financial analysis, provide professional investment recommendations. "
        "Consider market conditions and the company's financial health to suggest actionable strategies."
    ),
    expected_output=(
        "A professional investment recommendation report including potential entry/exit points and strategic rationale."
    ),
    agent=investment_advisor,
    tools=[analyze_investment_tool, search_tool],
)

# 4. Risk Assessment Task
risk_assessment = Task(
    description=(
        "Identify and evaluate potential risks associated with the investment. "
        "Analyze market volatility, operational challenges, and financial risks mentioned in the document."
    ),
    expected_output=(
        "A comprehensive risk profile highlighting key risks, their potential impact, and mitigation suggestions."
    ),
    agent=risk_assessor,
    tools=[create_risk_assessment_tool],
)