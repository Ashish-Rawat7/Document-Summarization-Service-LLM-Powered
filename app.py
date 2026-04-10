import streamlit as st
from document_loader import extract_text
from summarization import Summarizer

st.set_page_config(page_title="AI Document Summarizer", layout="centered")

st.title("AI Document Summarizer")

summarizer = Summarizer()

style = st.selectbox(
    "Summary Type",
    ["brief", "bullet", "detailed", "notes (1500+ words)"]
)

uploaded = st.file_uploader("Upload document", ["pdf", "txt", "docx"])
text_input = st.text_area("Or paste text", height=300)

if st.button("Generate Summary"):

    if uploaded:
        text = extract_text(uploaded)
    else:
        text = text_input.strip()

    if not text:
        st.error("Please provide input text")
        st.stop()

    with st.spinner("Generating summary..."):
        try:
            summary = summarizer.summarize(text, style)
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.stop()

    st.subheader("Summary")
    st.markdown(summary)

    st.download_button(
        "Download Summary",
        summary,
        file_name="summary.txt"
    )