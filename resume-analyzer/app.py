import os
import json
import streamlit as st

from dotenv import load_dotenv
from pypdf import PdfReader
from groq import Groq

#load env variables
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

#streamlit UI

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get ATS insights.")

#odf text extraction

def extract_text(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


#resume analysis

def analyze_resume(resume_text, target_role):

    prompt = f"""
You are an expert ATS Resume Analyzer.

Analyze the resume below for the target job role of '{target_role}'. Evaluate the match percentage and calculate an ATS score out of 100.

Resume:
{resume_text}

Return ONLY valid JSON.

{{
    "ats_score": 0, // Integer from 0 to 100 representing the match percentage out of 100
    "technical_skills": [],
    "strengths": [],
    "missing_skills": [],
    "suggestions": []
}}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


#file upload

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

#analyze button

if uploaded_file:

    resume_text = extract_text(uploaded_file)

    st.subheader("Resume Preview")

    st.text_area(
        "Extracted Text",
        resume_text[:2000],
        height=200
    )

    # Ask the user for the target job role
    target_role = st.text_input(
        "What job role/position are you applying for?",
        placeholder="e.g., Software Engineer, Product Manager, Data Scientist"
    )

    if st.button("Analyze Resume"):

        if not target_role.strip():
            st.error("⚠️ Please enter the target job role/position before starting the analysis.")
        else:
            with st.spinner("Analyzing Resume..."):

                result = analyze_resume(resume_text, target_role)

                try:

                    data = json.loads(result)

                    st.success("Analysis Complete!")

                    score = data["ats_score"]
                    st.metric(
                        "ATS Score",
                        f"{score}/100"
                    )
                    st.progress(score / 100.0)

                    st.subheader("Technical Skills")

                    for skill in data["technical_skills"]:
                        st.write(f"{skill}")

                    st.subheader("Strengths")

                    for strength in data["strengths"]:
                        st.write(f"{strength}")

                    st.subheader(" Missing Skills")

                    for skill in data["missing_skills"]:
                        st.write(f" {skill}")

                    st.subheader("Suggestions")

                    for suggestion in data["suggestions"]:
                        st.write(f"{suggestion}")

                except Exception:

                    st.subheader("Raw Response")

                    st.write(result)