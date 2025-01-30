from dotenv import load_dotenv
import os

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set. Check your .env file.")

os.environ["GROQ_API_KEY"] = api_key

# web search agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="mixtral-8x7b-32768"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

# financial agent

finance_agent = Agent(
    name="Financial Agent",
    model=Groq(id="mixtral-8x7b-32768"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
        )
    ],
    instructions=["use tables to display the data"],
    show_tools_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="mixtral-8x7b-32768"),
    instructions=["Always include sources", "use tables to display the data"],
    markdown=True,
    show_tools_calls=True,
)


finance_agent.print_response("What is the stock price of Tesla?", stream=True) #using financial agent to get financial data
 
web_search_agent.print_response("What does Nvidia do?", stream=True) #using web search agent to get web search data

multi_ai_agent.print_response("What is OpenAI?", stream=True) #using multi ai agent to get financial data and web search data

