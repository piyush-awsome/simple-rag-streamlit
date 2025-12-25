import streamlit as st
import os
from rag import create_vectorstore, answer_question

st.set_page_config(page_title="Simple RAG Demo")

st.title("📄 Simple RAG Demo")
st.write("Upload a PDF and ask questions")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    os.makedirs("data", exist_ok=True)

    pdf_path = "data/temp.pdf"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Processing document..."):
        vectorstore = create_vectorstore(pdf_path)

    question = st.text_input("Ask a question")

    if question:
        with st.spinner("Generating answer..."):
            answer = answer_question(vectorstore, question)

        st.success(answer)
