## Importing libraries and files
import os
from dotenv import load_dotenv

# Find the absolute path to the .env file in the current directory
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)
from crewai import Agent

 

from tools import search_tool, read_data_tool, analyze_investment_tool, create_risk_assessment_tool

from langchain_openai import ChatOpenAI

# Initialize LLM (using OpenAI as a default, assuming OPENAI_API_KEY is in .env)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)

# Creating a Senior Financial Analyst agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Provide accurate, data-driven financial analysis based on the provided document and query: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You are a seasoned financial analyst with expertise in corporate finance and market trends. "
        "Your analysis is known for its precision, objectivity, and deep understanding of financial statements. "
        "You focus on identifying key performance indicators, revenue growth, and profitability margins."
    ),
    tools=[read_data_tool, search_tool],
    llm=llm,
    max_iter=5,
    max_rpm=10,
    allow_delegation=True
)

# Creating a document verifier agent
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify the authenticity and relevance of financial documents to ensure they contain valid financial data.",
    verbose=True,
    memory=True,
    backstory=(
        "You have a background in financial compliance and auditing. Your role is to ensure that "
        "the documents provided are actual financial reports or statements and are relevant for analysis. "
        "You look for specific financial markers and headers to validate the document's content."
    ),
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=False
)

investment_advisor = Agent(
    role="Investment Strategy Advisor",
    goal="Provide professional investment recommendations based on the analysis of the financial document and query: {query}",
    verbose=True,
    backstory=(
        "You are an expert investment advisor with years of experience in portfolio management. "
        "Your recommendations are grounded in fundamental analysis and risk-adjusted return strategies. "
        "You provide actionable insights that align with market conditions and the company's financial health."
    ),
    tools=[analyze_investment_tool, search_tool],
    llm=llm,
    max_iter=5,
    max_rpm=10,
    allow_delegation=False
)

risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal="Identify and quantify potential risks associated with the investment based on the financial document.",
    verbose=True,
    backstory=(
        "You are a specialist in financial risk management. You analyze market risks, operational risks, "
        "and credit risks. Your goal is to provide a comprehensive risk profile to help investors "
        "make informed decisions by highlighting potential pitfalls and volatility."
    ),
    tools=[create_risk_assessment_tool],
    llm=llm,
    max_iter=5,
    max_rpm=10,
    allow_delegation=False
)
