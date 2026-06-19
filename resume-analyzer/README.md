# 📄 AI Resume Analyzer

An advanced, AI-powered Resume Analyzer built with Python, Streamlit, and Groq. This application extracts text from PDF resumes, compares it against a target job description or role, and evaluates the Applicant Tracking System (ATS) score. It also provides actionable feedback, including identified technical skills, strengths, missing skills, and suggestions for improvement.

---

## Features

- **PDF Text Extraction**: Seamlessly extracts raw text content from uploaded PDF resumes using `pypdf`.
- **Target Role Alignment**: Allows users to input a specific job role/position for customized evaluation.
- **ATS Match Scoring**: Calculates an ATS match score out of 100 based on the target role.
- **Detailed Insights**:
  - **Technical Skills**: Lists key technical competencies identified.
  - **Strengths**: Highlights areas where the resume shines for the target role.
  - **Missing Skills**: pinpoints critical skills and keywords that are absent.
  - **Suggestions**: Provides actionable recommendations to optimize the resume.
- **Modern Streamlit UI**: Offers a clean, intuitive, and responsive user interface.

---

## Tech Stack & Dependencies

- **Language**: Python 3.9+
- **Frontend Framework**: [Streamlit](https://streamlit.io/)
- **PDF Parser**: [pypdf](https://github.com/py-pdf/pypdf)
- **AI Engine**: [Groq Python SDK](https://github.com/groq/groq-python)
- **LLM Model**: `llama-3.3-70b-versatile`

---

## Prerequisites

Before running the project, ensure you have:
1. Python installed on your system.
2. A **Groq API Key**. You can get one from the [Groq Console](https://console.groq.com/).

---

## Installation & Setup

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd resume-analyzer
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # Activate on Windows:
   venv\Scripts\activate
   # Activate on macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install streamlit pypdf groq python-dotenv
   ```
   *(Alternatively, if you've populated `requirements.txt`, run `pip install -r requirements.txt`)*

4. **Configure Environment Variables**:
   Create a `.env` file in the root of the `resume-analyzer` directory and add your Groq API Key:
   ```env
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

---

## How to Run the Application

Start the Streamlit application by executing:
```bash
streamlit run app.py
```

Once started, open your browser and navigate to the local URL (usually `http://localhost:8501`).

---

##  Project Structure

```text
resume-analyzer/
├── app.py              # Main Streamlit application containing UI & logic
├── .env                # Local environment secrets (API Keys)
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## How it Works

1. **Text Extraction**: The app reads the PDF pages using `pypdf` and compiles the raw text content.
2. **ATS Querying**: The extracted resume text, alongside the target job role, is constructed into a prompt and dispatched to Groq's high-speed inference engine using the `llama-3.3-70b-versatile` model.
3. **Structured Response**: The model returns a strictly formatted JSON object detailing the scores and skill breakdown.
4. **UI Display**: The Streamlit interface displays the metrics and lists dynamically, offering a progress bar for the ATS score.
