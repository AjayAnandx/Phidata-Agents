import os 
from groq import Groq
from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.tavily import TavilyTools
from phi.llm.groq import Groq
from phi.tools.pubmed import PubmedTools
from phi.tools.newspaper4k import Newspaper4k
from phi.tools.apify import ApifyTools
from rich.pretty import pprint
from phi.assistant import Assistant, AssistantMemory


# Calling the LLM
Api_Key = str(input("Enter you Groq_API_Key : "))
llm = Groq(api_key=Api_Key, model_name="llama-3.1-405b",  )


# Writing all the agents for reasearch marketing

#Query summarizer
Query_Summarizer = Assistant(
    Name = "Query Reasearcher Agent",
    llm = llm,
    role = "Summarize the User query enter by the query and pass to the agent",
    Instruction = [
        "you will receive user queries as input.",
        "Want to analyze the query to understand its context, key points, and main ideas",
        "Want to generate a concise summary of the query. The summary should capture the essential information and intent of the query."
        "Output the summary to the user or the next processing agent."
    ]
)

# Market Reasearcher
Market_researchr = Assistant(
    Nmae = "Quantum Market_Reasearcher",
    llm = llm,
    Role = "Want to Conduct a reasearch on the query give by the user",
    Instruction = [
        """Identify key market trends, size, and growth rate.
           Analyze competitors, including their strengths, weaknesses, pricing strategies, and market positioning."""
    ],
    Tools = [TavilyTools(api_key="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",use_search_context=True),DuckDuckGo()],
)

# Article Reasearcher
Article_Reasearcher = Assistant(
    Name = "Quantum Article Reasearcher",
    llm = llm,
    Role = "want to search the artile for Based on the query",
    Tools = [PubmedTools(max_results=5,email= "ajaysunil35@gmail.com"),Newspaper4k(include_summary=True)],
    show_tool_calls = True
)

# Web Scraper
Web_Scraper = Assistant(
    Name  = "Quantum Web Scraper",
    llm = llm,
    Role = "scrap the web for the content",
    Instruction = ["""URL(s): [List the URLs to be scraped]
                   Note: Ensure you have permission to scrape the target websites."""],
    Tools = [ApifyTools(api_key = "apify_api_Yh9HcZdEiygVOFAmUCheNgqRn7BvI734G9Vm")]
)

# Content Summarizer
Content_Summarizer = Assistant(
    Name  = "Quantum Content Researcher",
    llm = llm,
    Role = "want to summarize the content give by the assistant "

)

# Content writer
Content_Writer = Assistant(
    Name = "Quantum Content Reasearcher ",
    llm = llm,
    Role = "Write A report on Query",
    Tools  = []
)

# Calling alll the tolls and combine as a one agent
Quantum_Assistant = Assistant(
    Name  = "Quantum Marketing Assistant",
    markdown = True,
    Teams = [Query_Summarizer,Content_Writer,Article_Reasearcher,Market_researchr,Content_Summarizer],
    llm = llm,
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

# To print the Memory of the LLm
memory: AssistantMemory = Quantum_Assistant.memory
# -*- Print Chat History
print("============ Chat History ============")
pprint(memory.chat_history)








