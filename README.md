# 📚 ResearchMate AI

ResearchMate AI is a Multi-Agent AI Research Assistant that helps researchers, students, and academicians analyze research papers automatically.

Users can upload a research paper PDF and instantly generate:

- 📄 Research Summary
- 🔍 Research Gaps
- 🎯 Interview & Viva Questions
- 📊 PowerPoint Presentation Outline
- 📈 Research Quality Scorecard
- 💬 Chat with Research Paper
- 📥 Downloadable PPT
- 📥 Downloadable Research Report

---

## 🚀 Features

### 📄 Summary Agent
Generates:

- Paper Title
- Research Objective
- Methodology
- Dataset Used
- Results
- Key Contributions

---

### 🔍 Research Gap Agent

Identifies:

- Research Gaps
- Study Limitations
- Missing Experiments
- Future Research Directions
- Novel Improvement Ideas

---

### 🎯 Interview Agent

Generates:

- Basic Questions
- Technical Questions
- Research Questions
- Viva Questions

---

### 📊 PPT Agent

Automatically creates:

- Introduction
- Problem Statement
- Objectives
- Methodology
- Dataset
- Results
- Research Gaps
- Future Scope
- Conclusion

Downloadable as:

```text
ResearchMate_Presentation.pptx
```

---

### 📈 Scorecard Agent

Acts as a Research Reviewer and evaluates:

- Novelty
- Technical Complexity
- Dataset Quality
- Deployment Readiness
- Research Impact

---

### 📄 Metadata Agent

Extracts:

- Title
- Authors
- Publication Year
- DOI
- Keywords

---

### 💬 Chat Agent

Allows users to ask questions directly about the uploaded paper.

Example:

```text
What dataset was used?
What is the proposed methodology?
What are the main findings?
```

---

### 📥 Report Generator

Creates a complete research report including:

- Summary
- Research Gaps
- Interview Questions
- PPT Outline

Downloadable as:

```text
Research_Report.docx
```

---

## 🏗️ Project Architecture

```text
PDF Upload
      │
      ▼
PDF Reader + OCR
      │
      ▼
ResearchMate AI
      │
 ┌────┼────┐
 │    │    │
 ▼    ▼    ▼

Metadata Agent
Summary Agent
Gap Agent
Interview Agent
PPT Agent
Scorecard Agent
Chat Agent

      │
      ▼

PPT Generator
Report Generator
```

---

## 🛠️ Tech Stack

### Frontend

- Streamlit

### AI Models

- OpenRouter API
- OpenAI Compatible Client

### PDF Processing

- PyMuPDF (fitz)
- Tesseract OCR
- pdf2image

### Document Generation

- python-pptx
- python-docx

### Environment

- Python 3.13

---

## 📂 Project Structure

```text
ResearchMate-AI
│
├── app.py
├── config.py
├── requirements.txt
│
├── agents
│   ├── chat_agent.py
│   ├── summary_agent.py
│   ├── gap_agent.py
│   ├── interview_agent.py
│   ├── metadata_agent.py
│   ├── ppt_agent.py
│   └── scorecard_agent.py
│
├── utils
│   ├── pdf_reader.py
│   ├── ppt_generator.py
│   └── report_generator.py
│
└── data
```

---

## ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/Harika-1305/ResearchMate-AI.git
```

Move into project:

```bash
cd ResearchMate-AI
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 👩‍💻 Author

**Bhogi Harika**

B.Tech – Computer Science & Information Technology (CSIT)

Maharaj Vijayaram Gajapathi Raj College of Engineering (MVGR)

GitHub:
https://github.com/Harika-1305

---

## ⭐ Future Enhancements

- Research Paper Recommendation System
- Multi-PDF Comparison
- Citation Generator
- Literature Review Generator
- RAG-Based Research Assistant
- Research Trend Analysis