import os

from dotenv import find_dotenv, load_dotenv

from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain
from langchain_experimental.utilities import PythonREPL
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.utilities.wolfram_alpha import WolframAlphaAPIWrapper
from langchain_community.tools import WikipediaQueryRun, WolframAlphaQueryRun, Tool

import streamlit as st


# Load environment variables
load_dotenv(find_dotenv())

# Get API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
WOLFRAM_ALPHA_APPID = os.getenv("WOLFRAM_ALPHA_APPID")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Initialize LLM
llm_model = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.3-70b-versatile")

# Wikipedia Tool
wikipedia_api_wrapper = WikipediaAPIWrapper()
wikipedia_query_run = WikipediaQueryRun(api_wrapper=wikipedia_api_wrapper)
wikipedia_tool = Tool(name="wikipedia_search",
                      func=wikipedia_query_run.run,
                      description="Search Wikipedia for factual information.")

# Python REPL Tool (for executing Python code)
pythoneprl = PythonREPL()
pythonrepl_tool = Tool(name="python_repl",
                       func=pythoneprl.run,
                       description="Executes Python code inside a REPL environment.")

# Math Computation Tool
llmmaths = LLMMathChain.from_llm(llm=llm_model)
llmmaths_tool = Tool(name="math_calculator",
                     func=llmmaths.run,
                     description="Performs numerical computations and solves equations.")

# Wolfram Alpha Tool
wolfram_api_wrapper = WolframAlphaAPIWrapper(wolfram_alpha_appid=WOLFRAM_ALPHA_APPID)
wolfram_query_run = WolframAlphaQueryRun(api_wrapper=wolfram_api_wrapper)
wolfram_tool = Tool(name="wolfram_alpha",
                    func=wolfram_query_run.run,
                    description="Query Wolfram Alpha for advanced computations.")

# Tavily Search tool
tavily_search = TavilySearchResults(max_results=10, 
                                    search_depth="advanced")

tavily_search_tool = Tool(name="tavily search tool", 
                          func=tavily_search.run, 
                          description="Query Tavily Search API for retrieving real-time search results from the web.")

prompt = ChatPromptTemplate.from_messages([
    ("system", (
                "You are Eddy, an AI assistant designed to help with calculations"
                "Wikipedia searches, and real-time information retrieval."
                "Your goal is to provide accurate, efficient, and insightful responses to assist users in their queries")
                ),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("user", "{user_input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

tools = [wikipedia_tool, pythonrepl_tool, llmmaths_tool, wolfram_tool, tavily_search_tool]

tool_calling_agent = create_tool_calling_agent(llm=llm_model,
                                               prompt=prompt,
                                               tools=tools)

AGENT_1 = AgentExecutor(agent=tool_calling_agent, 
                        tools=tools, 
                        verbose=True, 
                        handle_parsing_errors=True)

# print(AGENT_1.invoke({"user_input":"whats the most streamed music on billboard"}))