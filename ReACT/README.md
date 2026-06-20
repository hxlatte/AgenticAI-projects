# AI Research Assistant

AI Research Assistant is a Streamlit-based Agentic AI application that performs in-depth research on any topic using multiple knowledge sources. The system combines ReAct-based reasoning with web search, Wikipedia, and Arxiv research papers to generate structured reports and downloadable PDF summaries.

## Features

* ReAct-based AI Agent
* Multi-source Research

  * Tavily Web Search
  * Wikipedia
  * Arxiv Research Papers
* Adjustable Research Depth

  * Basic
  * Detailed
  * Deep
* Structured Research Reports
* Source References
* PDF Report Download
* Interactive Streamlit Interface

## Tech Stack

### Frontend

* Streamlit

### AI & Agent Framework

* LangChain
* LangChain Classic Agents
* Groq
* Llama 3.3 70B Versatile

### Research Sources

* Tavily Search API
* Wikipedia API
* Arxiv API

### Utilities

* Python Dotenv
* ReportLab

## Project Structure

```text
ReACT/
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd ReACT
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Running the Application

```bash
streamlit run app.py
```

## How It Works

1. User enters a research topic.
2. The ReAct Agent plans its reasoning process.
3. The agent gathers information from selected sources.
4. Information is synthesized into a structured report.
5. Sources are displayed for reference.
6. The report can be downloaded as a PDF.

## Sample Research Report Structure

* Executive Summary
* Key Findings
* Benefits
* Challenges
* Future Trends
* Conclusion
* References

## Future Enhancements

* Chat History
* Citation Generation
* Multi-Agent Workflows with LangGraph
* Research Planner Agent
* Fact Verification Agent
* PDF Formatting Improvements
* Report Export in DOCX Format

## Author

Kasani Hansika Goud

Computer Science Engineering Student | MERN Developer | AI & Agentic AI Enthusiast
