import os
from dotenv import load_dotenv
load_dotenv()
import requests
from bs4 import BeautifulSoup
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


@tool
def scraper(url:str):
    """Fetch a webpage and extract its readable text."""

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )
        response.raise_for_status()
    except requests.RequestException:
        return ""

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove things that aren't useful research content
    for element in soup([
        "script",
        "style",
        "nav",
        "footer",
        "header",
        "aside"
    ]):
        element.decompose()

    text = soup.get_text(separator=" ", strip=True)

    return text

tools = [scraper]

prompt = """
You are the Web Content Extraction Agent in a multi-agent research system.

Your task is to extract useful research information from a webpage
using the scraper tool.

...

Do not write the final research report.
Do not combine information from different sources into conclusions.
Do not invent information.
"""


llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.2,
    max_tokens=1024,
)

agent = create_agent(model=llm, tools=tools, system_prompt=prompt)





def get_content(sharedmemory):
    print("starting reader_agent")
    for url in sharedmemory["urls"]:
        print("working on", (url))
        try:
            result = agent.invoke({
            "messages": [
                        {
                            "role": "user",
                            "content": f"""
                            Research question:
                            {sharedmemory["question"]}

                            Scrape and extract useful information from this URL:
                            {url}
                            """
                        }
                    ]
                })
            content = result["messages"][-1].content
            if content:
                sharedmemory["content"].append(content)
            print("done working on", (url))
        except Exception as exc:
            print(f"skipping blocked/failed URL: {url} ({exc})")

    return sharedmemory

