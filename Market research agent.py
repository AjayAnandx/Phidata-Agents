import os 
from groq import Groq
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.searxng import Searxng
from phi.model.groq import Groq
from phi.tools.newspaper4k import Newspaper4k
from phi.tools.apify import ApifyTools
from phi.tools.arxiv_toolkit import ArxivToolkit
from rich.pretty import pprint
from phi.tools.crawl4ai_tools import Crawl4aiTools
from phi.tools.website import WebsiteTools
from phi.tools.file import FileTools

# Calling the LLM
llm = Groq(id="llama3-groq-70b-8192-tool-use-preview",api_key="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"  )

Query_Splliter = Agent (
    name  = "query splitter",
    model = llm,
    role  = "to split the key details in the query",
    instructions = ["Split the query into the key point"
    "1. Url"
    "2. Topic"
    "3. content"],
)

searxng = Searxng(
    host="http://localhost:53153",
    engines=["goole"],
    it=True,
    fixed_max_results=5,
    news=True,
    science=True
)

Research_Agent = Agent(
    name = "Research Agent",
    model = llm,
    role  = "research the about the user {query}",
    tools = [Crawl4aiTools(max_length=1000)],
)

Web_searcher = Agent(
    name = "web scraper",
    mnodel = llm,
    tools = [searxng],
)

Article_finder = Agent(
    name = "Article finder",
    model = llm,
    role = "To get the paper links from the arvix",
    tool = [ArxivToolkit(search_arxiv=True)],
)

Article_reader = Agent(
    name = "Article reader",
    model = llm,
    role = "to read the Arvix paper",
    tools = [ArxivToolkit(read_arxiv_papers=True)],
)

Report_Writer  = Agent(
    name = "Report Writer",
    model = llm,
    role = "to write a reoport on the query",
)

Quantum_Assistant = Agent(
    name  = "report Genetrator",
    model = llm,
    role = "to lead the team of agents",
    tool = [Report_Writer,Article_reader,Web_searcher,Research_Agent,FileTools,Query_Splliter],
    instructions = [
        "Lead the team of agents and guide them to use the correct usage for the user query"
        "drive the final Report"
        "Note: if the user pecify a agent only use them"
    ],
    markdown = True,
    show_tools_call = True,
)

# looping the statement
while True:
    Query = str(input("Enter The Query (or 'exit' to stop): "))
    # if the user type exit the loop will end
    if Query.lower() =='exit':
        break
    response = Quantum_Assistant.print_response(Query)
    print(response)
#if the api does not functio return this message
else :
    print("the System is not responding Please Refersh it")
