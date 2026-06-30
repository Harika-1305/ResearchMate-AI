from agents.summary_agent import generate_summary
from agents.gap_agent import generate_research_gaps
from agents.interview_agent import generate_interview_questions

import streamlit as st
from utils.pdf_reader import extract_text

st.set_page_config(
    page_title="ResearchMate AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 ResearchMate AI")
st.write("Upload a research paper and generate AI-powered insights.")

# Upload PDF
pdf = st.file_uploader(
    "Upload Research Paper",
    type=["pdf"]
)

if pdf is not None:

    st.success("PDF Uploaded Successfully")

    # Extract Text
    text = extract_text(pdf)

    st.write(f"**Text Length:** {len(text)} characters")

    # Display Extracted Text
    st.subheader("Extracted Text")

    st.text_area(
        "Paper Content",
        value=text[:5000],
        height=400
    )

    # Three Buttons in One Row
    col1, col2, col3 = st.columns(3)

    # -------------------------
    # SUMMARY AGENT
    # -------------------------
    with col1:

        if st.button("📄 Generate Summary"):

            if len(text.strip()) == 0:

                st.error("No text extracted from PDF.")

            else:

                with st.spinner("Analyzing Paper..."):

                    try:

                        summary = generate_summary(text)

                        st.subheader("📄 Paper Summary")

                        st.markdown(summary)

                    except Exception as e:

                        st.error(
                            f"Error generating summary: {str(e)}"
                        )

    # -------------------------
    # RESEARCH GAP AGENT
    # -------------------------
    with col2:

        if st.button("🔍 Find Research Gaps"):

            if len(text.strip()) == 0:

                st.error("No text extracted from PDF.")

            else:

                with st.spinner("Finding Research Gaps..."):

                    try:

                        gaps = generate_research_gaps(text)

                        st.subheader(
                            "🔍 Research Gaps & Future Scope"
                        )

                        st.markdown(gaps)

                    except Exception as e:

                        st.error(
                            f"Error generating gaps: {str(e)}"
                        )

    # -------------------------
    # INTERVIEW AGENT
    # -------------------------
    with col3:

        if st.button("🎯 Generate Questions"):

            if len(text.strip()) == 0:

                st.error("No text extracted from PDF.")

            else:

                with st.spinner("Generating Questions..."):

                    try:

                        questions = generate_interview_questions(text)

                        st.subheader(
                            "🎯 Interview & Viva Questions"
                        )

                        st.markdown(questions)

                    except Exception as e:

                        st.error(
                            f"Error generating questions: {str(e)}"
                        )