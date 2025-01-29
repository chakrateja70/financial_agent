from dotenv import load_dotenv
import os

# Load model directly
from transformers import AutoModel
model = AutoModel.from_pretrained("deepseek-ai/Janus-Pro-7B")

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set. Check your .env file.")

# Set the environment variable explicitly
os.environ["GROQ_API_KEY"] = api_key

# web search agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

# financial agent

finance_agent = Agent(
    name="Financial Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
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

#multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for Nvidia", stream=True)

try:
    multi_ai_agent.print_response("What does Nvidia do?", stream=True)
except Exception as e:
    print("An error occurred:", e)

