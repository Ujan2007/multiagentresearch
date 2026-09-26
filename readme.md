# 🔬 Multi-Agent Research Agent

Use the application at --> https://deepresearch99.streamlit.app/

A multi-agent AI research system that takes a research question, searches the web for relevant sources, extracts useful information from those sources, and synthesizes everything into a structured research report.

The project is built using **LangChain, LangGraph, Hugging Face, Mistral, Tavily, BeautifulSoup, and Streamlit**.

The main goal of this project is to explore how a complex research task can be divided between multiple specialized AI components, with each component responsible for a specific stage of the research process.

---

## ✨ Features

- 🔎 Web search using Tavily
- 🤖 Multi-agent architecture
- 🌐 Webpage extraction using Requests + BeautifulSoup
- 🧠 LLM-based information extraction
- 📝 Automatic research synthesis
- 🔗 Source preservation
- 💾 Shared memory between agents
- 🖥️ Streamlit web interface
- 📊 Source and processing statistics
- 🔄 Modular architecture

---

# 🏗️ Architecture

The system consists of three main stages.

```text
                         USER
                           │
                           ▼
                  ┌─────────────────┐
                  │  Streamlit UI   │
                  └────────┬────────┘
                           │
                           │ Research Question
                           ▼
                  ┌─────────────────┐
                  │    AGENT 1      │
                  │ Source Discovery│
                  └────────┬────────┘
                           │
                           │ Question + URLs
                           ▼
                  ┌─────────────────┐
                  │    AGENT 2      │
                  │ Web Content     │
                  │ Extraction      │
                  └────────┬────────┘
                           │
                           │ Extracted Content
                           ▼
                  ┌─────────────────┐
                  │    AGENT 3      │
                  │ Research Writer │
                  └────────┬────────┘
                           │
                           │ Final Research
                           ▼
                  ┌─────────────────┐
                  │ Research Report │
                  └─────────────────┘
# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **LangChain** | LLM integrations, tools, agents, prompts, and runnables |
| **LangGraph** | Agent execution and orchestration infrastructure used internally by LangChain agents |
| **Hugging Face** | Hosted inference for the Qwen model |
| **Qwen** | Source discovery and research synthesis |
| **Mistral** | Web content extraction and analysis |
| **Tavily** | Web search and source discovery |
| **Requests** | Fetching webpage HTML |
| **BeautifulSoup** | Parsing and cleaning webpage content |
| **Streamlit** | Web-based user interface |
| **python-dotenv** | Loading API credentials from environment variables |

---

# 📦 Packages

The main Python packages used in this project are:

```text
langchain
langgraph
langchain-openai
langchain-mistralai
langchain-tavily
tavily-python
beautifulsoup4
requests
python-dotenv
streamlit
```

All dependencies can be installed using:

```bash
pip install -r requirements.txt
```

# 🧠 Shared Memory

A central part of the architecture is the use of a shared Python dictionary called `sharedmemory`.

Instead of having each agent operate independently, the agents communicate through this shared state. Each stage reads the information produced by the previous stage and adds its own results without discarding the existing information.

The initial state is:

```python
sharedmemory = {
    "question": "",
    "urls": [],
    "content": []
}

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd multiagent-research
```

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

The project requires API credentials for the external services used by the agents.

Create a `.env` file in the root directory:

```env
HF_TOKEN=your_huggingface_token
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Make sure the `.env` file is included in `.gitignore`:

```text
.env
venv/
.venv/
__pycache__/
```

> **Never commit your API keys to GitHub.**

---

# ▶️ Running the Project

## Command Line Interface

The original backend pipeline can be run directly from the project root:

```bash
python main.py
```

You will be prompted to enter a research question:

```text
What would you like to dive into today?
```

The complete pipeline will then execute:

```text
Research Question
       │
       ▼
Source Discovery
       │
       ▼
Web Content Extraction
       │
       ▼
Research Synthesis
       │
       ▼
Final Research Report
```

---

## Streamlit Interface

The project also includes a web-based interface.

From the project root, run:

```bash
streamlit run ui/app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

The Streamlit interface provides:

- Research question input
- Research execution
- Agent pipeline status
- Number of sources discovered
- Number of sources analyzed
- Links to the discovered sources
- Final synthesized research report

---

# ⚠️ Research Scope

The number of web sources searched and analyzed by the system is intentionally limited.

This limitation is primarily due to **API usage and key constraints** associated with the external services used by the project.

The source limit is therefore a **deployment/API constraint rather than a fundamental limitation of the architecture**.

The underlying architecture can be extended to process a significantly larger number of sources when higher API limits and additional resources are available.

For example, the current workflow can conceptually scale from:

```text
Question
   │
   ├── Source 1
   ├── Source 2
   ├── Source 3
   └── Source 4
```

to a much larger research set:

```text
Question
   │
   ├── Source 1
   ├── Source 2
   ├── Source 3
   ├── Source 4
   ├── Source 5
   ├── ...
   └── Source N
```

The current limit is intentionally kept conservative to work within available API constraints.

---

# 🎯 Project Objective

The primary objective of this project was to explore how a complex research task can be decomposed into **multiple specialized AI components** instead of relying on a single LLM call.

The system divides the research process into three distinct responsibilities:

```text
Search → Extract → Synthesize
```

Each stage has a specific role:

### 1. Search

Discover relevant information sources from the web.

### 2. Extract

Retrieve webpages and extract information relevant to the original research question.

### 3. Synthesize

Combine the extracted information into a coherent and structured research report.

The agents communicate through a shared state, allowing information generated by one stage to become the input for the next.

This modular architecture also makes it possible to independently replace or improve individual components — such as the search provider, LLM, scraping method, or synthesis stage — without redesigning the entire system.

Ultimately, the project was built to demonstrate a practical implementation of a **multi-agent research workflow**, while also exploring concepts such as:

- LLM tool calling
- AI agents
- Shared state
- LangChain agents
- LangChain runnables
- LLM pipelines
- Web search
- Web scraping
- Information extraction
- Multi-stage LLM synthesis
