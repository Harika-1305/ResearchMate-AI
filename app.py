from agents.summary_agent import generate_summary
from agents.gap_agent import generate_research_gaps
from agents.interview_agent import generate_interview_questions
from agents.chat_agent import chat_with_paper
from agents.ppt_agent import generate_ppt
from agents.metadata_agent import extract_metadata
from agents.scorecard_agent import generate_scorecard

from utils.pdf_reader import extract_text
from utils.ppt_generator import create_ppt
from utils.report_generator import create_report

import streamlit as st


st.set_page_config(
    page_title="ResearchMate AI",
    page_icon="📚",
    layout="wide"
)

# =====================================
# HEADER
# =====================================

st.title("📚 ResearchMate AI")

st.write(
    "Upload a research paper and generate AI-powered insights."
)

# =====================================
# FILE UPLOAD
# =====================================

pdf = st.file_uploader(
    "Upload Research Paper",
    type=["pdf"]
)

# =====================================
# PDF PROCESSING
# =====================================

if pdf is not None:

    st.success("PDF Uploaded Successfully")


    text = extract_text(pdf)

    st.write(
        f"**Text Length:** {len(text)} characters"
    )

    st.write(
        f"**Text Length:** {len(text)} characters"
    )

    # =====================================
    # PAPER METADATA
    # =====================================

    with st.expander(
        "📄 Paper Information",
        expanded=True
    ):

        try:

            metadata = extract_metadata(text)

            st.markdown(metadata)

        except Exception as e:

            st.error(
                f"Metadata Extraction Error: {str(e)}"
            )

    # =====================================
    # EXTRACTED TEXT
    # =====================================

    st.subheader("Extracted Text")

    st.text_area(
        "Paper Content",
        value=text[:5000],
        height=400
    )

    # =====================================
    # TABS
    # =====================================

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
        [
            "📄 Summary",
            "🔍 Gaps",
            "🎯 Questions",
            "📊 PPT",
            "📈 Score",
            "📄 Report",
            "💬 Chat"
        ]
    )

    # =====================================
    # SUMMARY
    # =====================================

    with tab1:

        if st.button(
            "Generate Summary"
        ):

            with st.spinner(
                "Generating Summary..."
            ):

                try:

                    summary = generate_summary(
                        text
                    )

                    st.markdown(
                        summary
                    )

                except Exception as e:

                    st.error(
                        str(e)
                    )

    # =====================================
    # RESEARCH GAPS
    # =====================================

    with tab2:

        if st.button(
            "Find Research Gaps"
        ):

            with st.spinner(
                "Finding Research Gaps..."
            ):

                try:

                    gaps = generate_research_gaps(
                        text
                    )

                    st.markdown(
                        gaps
                    )

                except Exception as e:

                    st.error(
                        str(e)
                    )

    # =====================================
    # QUESTIONS
    # =====================================

    with tab3:

        if st.button(
            "Generate Questions"
        ):

            with st.spinner(
                "Generating Questions..."
            ):

                try:

                    questions = generate_interview_questions(
                        text
                    )

                    st.markdown(
                        questions
                    )

                except Exception as e:

                    st.error(
                        str(e)
                    )

    # =====================================
    # PPT
    # =====================================

    with tab4:

        if st.button(
            "Generate PPT"
        ):

            with st.spinner(
                "Generating Presentation..."
            ):

                try:

                    ppt_content = generate_ppt(
                        text
                    )

                    st.markdown(
                        ppt_content
                    )

                    ppt_file = create_ppt(
                        ppt_content
                    )

                    with open(
                        ppt_file,
                        "rb"
                    ) as file:

                        st.download_button(
                            label="📥 Download PPT",
                            data=file,
                            file_name="ResearchMate_Presentation.pptx",
                            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                        )

                except Exception as e:

                    st.error(
                        str(e)
                    )

    # =====================================
    # SCORECARD
    # =====================================

    with tab5:

        if st.button(
            "Generate Scorecard"
        ):

            with st.spinner(
                "Evaluating Research..."
            ):

                try:

                    score = generate_scorecard(
                        text
                    )

                    st.markdown(
                        score
                    )

                except Exception as e:

                    st.error(
                        str(e)
                    )

    # =====================================
    # REPORT
    # =====================================

    with tab6:

        if st.button(
            "Generate Full Report"
        ):

            with st.spinner(
                "Generating Report..."
            ):

                try:

                    summary = generate_summary(
                        text
                    )

                    gaps = generate_research_gaps(
                        text
                    )

                    questions = generate_interview_questions(
                        text
                    )

                    ppt = generate_ppt(
                        text
                    )

                    report_file = create_report(
                        summary,
                        gaps,
                        questions,
                        ppt
                    )

                    with open(
                        report_file,
                        "rb"
                    ) as file:

                        st.download_button(
                            label="📥 Download Report",
                            data=file,
                            file_name="Research_Report.docx",
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                        )

                except Exception as e:

                    st.error(
                        str(e)
                    )

    # =====================================
    # CHAT WITH PAPER
    # =====================================

    with tab7:

        st.subheader(
            "💬 Chat With Paper"
        )

        question = st.text_input(
            "Ask anything about the paper"
        )

        if st.button(
            "Ask Question"
        ):

            if question.strip() == "":

                st.warning(
                    "Please enter a question."
                )

            else:

                with st.spinner(
                    "Thinking..."
                ):

                    try:

                        answer = chat_with_paper(
                            text,
                            question
                        )

                        st.markdown(
                            answer
                        )

                    except Exception as e:

                        st.error(
                            str(e)
                        )