import streamlit as st
from document_loader import extract_text
from summarization import Summarizer

st.set_page_config("Document Summarizer", layout="centered")
st.title("Document Summarization Service")

summarizer = Summarizer()

style = st.selectbox(
    "Output type",
    ["brief", "bullet", "detailed", "notes (1500+ words)"]
)
uploaded = st.file_uploader("Upload document", ["pdf", "txt", "docx"])
text_input = st.text_area("Or paste text", height=300)

if st.button("Generate Summary"):
    try:
        if uploaded:
            text = extract_text(uploaded)
        else:
            text = text_input.strip()

        if not text:
            st.error("No text provided")
            st.stop()

        with st.spinner("Summarizing..."):
            summary = summarizer.summarize(text)

        st.subheader("Summary")
        st.write(summary)
        st.download_button("Download", summary, "summary.txt")

    except Exception as e:
        st.error(str(e))
