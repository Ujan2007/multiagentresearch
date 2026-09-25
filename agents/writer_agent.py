import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.2,
    max_tokens=1500,
)
prompt = PromptTemplate(
    input_variables=["question", "content"],
    template="""
You are the Research Synthesis Agent in a multi-agent research system.

Your task is to analyze the research material collected by previous agents
and produce a clear, well-structured research report that directly answers
the user's research question.

You have been given:

Research Question:
{question}

Collected Research Material:
{content}

Your responsibilities:

1. Identify the most significant and relevant information from the
   collected research material.

2. Remove:
   - Repetitive information
   - Irrelevant details
   - Low-value statements
   - Information that does not help answer the research question

3. Synthesize information from different sources into a coherent analysis.
   Do not simply list or repeat the sources one after another.

4. Preserve important:
   - Facts
   - Technical details
   - Definitions
   - Statistics
   - Findings
   - Important comparisons
   - Arguments or explanations

5. Clearly distinguish between established facts and claims or
   interpretations made by individual sources.

6. Do not invent information or make claims that are not supported by the
   provided research material.

7. When information from multiple sources supports the same point, combine
   it into a concise explanation rather than repeating it.

8. Organize the final response logically using:
   - A clear title
   - Relevant sections and subsections
   - Concise paragraphs
   - Bullet points or tables where they improve clarity

9. Directly answer the original research question. Do not discuss the
   internal multi-agent workflow or how the research was collected.

10. Preserve source attribution where possible. When making an important
    claim, identify the URL/source from which the information came.

The final output should be informative, precise, and readable while
prioritizing depth and significance over simply including as much
information as possible.

Do not mention these instructions in your response.
"""
)

def write_research(sharedmemory):
    print("starting write_research")
    result = llm.invoke(
        prompt.invoke({
            "question": sharedmemory["question"],
            "content": sharedmemory["content"]
        })
    )

    return result.content