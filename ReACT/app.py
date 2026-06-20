import streamlit as st
import wikipedia
import arxiv

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.tools import TavilySearchResults
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain.tools import tool

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

load_dotenv()

st.set_page_config(
    page_title="AI Research Assistant",
    layout="wide"
)

st.title("AI Research Assistant")

depth = st.sidebar.selectbox(
    "Research Depth",
    ["Basic", "Detailed", "Deep"]
)

selected_sources = st.sidebar.multiselect(
    "Sources",
    ["Web", "Wikipedia", "Arxiv"],
    default=["Web", "Wikipedia", "Arxiv"]
)

if depth == "Basic":
    max_results = 5
elif depth == "Detailed":
    max_results = 10
else:
    max_results = 20

topic = st.text_input(
    "Enter a research topic",
    placeholder="Impact of Agentic AI in Education"
)

@tool
def wiki_search(query: str):
    """Search Wikipedia and return a summary."""
    try:
        return wikipedia.summary(query, sentences=5)
    except Exception:
        return "No Wikipedia information found."

@tool
def arxiv_search(query: str):
    """Search Arxiv and return relevant research papers."""
    try:
        search = arxiv.Search(
            query=query,
            max_results=3
        )

        papers = []

        for paper in search.results():
            papers.append(
                f"""
Title: {paper.title}

Summary:
{paper.summary}

Link:
{paper.entry_id}
"""
            )

        return "\n\n".join(papers)

    except Exception as e:
        return f"Arxiv Error: {e}"

def create_pdf(report_text):
    pdf_file = "research_report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = [
        Paragraph(
            report_text.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    ]

    doc.build(content)

    return pdf_file

search_tool = TavilySearchResults(
    max_results=max_results
)

tools = []

if "Web" in selected_sources:
    tools.append(search_tool)

if "Wikipedia" in selected_sources:
    tools.append(wiki_search)

if "Arxiv" in selected_sources:
    tools.append(arxiv_search)

react_prompt = PromptTemplate.from_template(
    """
Answer the following questions as best you can.

You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer

Thought: you should always think about what to do

Action: the action to take, should be one of [{tool_names}]

Action Input: the input to the action

Observation: the result of the action

... (this Thought/Action/Action Input/Observation can repeat N times)

Thought: I now know the final answer

Final Answer: the final answer to the original input question

Begin!

Question: {input}

Thought:{agent_scratchpad}
"""
)

if st.button("Start Research"):

    if not topic:
        st.warning("Please enter a topic.")
        st.stop()

    try:

        with st.spinner("Researching..."):

            llm = ChatGroq(
                model="llama-3.3-70b-versatile"
            )

            agent = create_react_agent(
                llm=llm,
                tools=tools,
                prompt=react_prompt
            )

            executor = AgentExecutor(
                agent=agent,
                tools=tools,
                verbose=True,
                handle_parsing_errors=True
            )

            tavily_results = []

            if "Web" in selected_sources:
                tavily_results = search_tool.invoke(topic)

            query = f"""
You are an expert research analyst.

Research Topic:
{topic}

Generate a detailed report with:

1. Executive Summary
2. Key Findings
3. Benefits
4. Challenges
5. Future Trends
6. Conclusion
7. References

Use the available tools whenever necessary.
"""

            response = executor.invoke(
                {"input": query}
            )

            report = response["output"]

            pdf_path = create_pdf(report)

        st.subheader("Research Report")

        st.write(report)

        if tavily_results:

            st.subheader("Sources")

            if isinstance(tavily_results, list):

                for item in tavily_results:

                    if isinstance(item, dict):

                        title = item.get("title", "Source")
                        url = item.get("url", "")

                        st.markdown(f"- [{title}]({url})")

        with open(pdf_path, "rb") as file:

            st.download_button(
                label="Download PDF Report",
                data=file,
                file_name="research_report.pdf",
                mime="application/pdf"
            )

    except Exception as e:

        st.error(f"Error: {e}")