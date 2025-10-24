import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("AskNotes — AI Note Summarizer & Quiz")
uploaded_file = st.file_uploader("Upload your notes (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:
    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    with st.spinner("Processing..."):
        res = requests.post(f"{API_URL}/upload", files=files)
        if res.status_code == 200:
            data = res.json()
            st.subheader("Summary")
            st.write(data["summary"])
            st.subheader("Quiz")
            st.write(data["quiz"])
        else:
            st.error("Error: " + res.text)
