import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
import json
from langchain_openai import ChatOpenAI

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

search = TavilySearch(max_results=10)


@tool
def web_search(topic: str):
    """Search the web for a given topic and return the results."""
    return search.invoke({"query": topic})


tools = [web_search]

sharedmemory = {"question": "", "urls": [], "content": []}

llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.2,
    max_tokens=1024,
)

prompt = """
You are the Source Discovery Agent in a multi-agent research system.

Your task is to find relevant and reliable web sources for the user's
research question.

Use the web_search tool to search the web.

Prioritize:
- Research papers and academic sources
- Official documentation and primary sources
- Reputable research organizations
- High-quality technical sources

Avoid:
- Low-quality SEO content
- Irrelevant pages
- Duplicate sources

Do not answer the research question.
Do not summarize the sources.
Do not scrape webpage content.

After searching, return the 10 most relevant unique URLs you found.
You MUST return up to 8-10 URLs whenever 6 relevant sources are available.

After completing your searches, return ONLY valid JSON in this exact format:

{
    "question": "the original research question",
    "urls": [
        "https://example.com/source1",
        "https://example.com/source2"
    ]
}

Do not include markdown.
Do not include ```json.
Do not include any explanation outside the JSON.
"""

agent = create_agent(model=llm, tools=tools, system_prompt=prompt)


def get_search_agent(content: str):
    print("starting search_agent")

    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": content,
            }
        ]
    })

    try:
        payload = result["messages"][-1].content
        sources = json.loads(payload)
        urls = sources.get("urls", [])
        question = sources.get("question", content)
    except Exception:
        urls = []
        question = content

    if not urls:
        direct = search.invoke({"query": content})
        urls = [item.get("url") for item in direct.get("results", []) if item.get("url")]

    sharedmemory["question"] = question
    sharedmemory["urls"] = urls

    print(sharedmemory)
    return sharedmemory

