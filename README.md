# Simple RAG (Retrieval-Augmented Generation) Demo

This project is a **simple, end-to-end Retrieval-Augmented Generation (RAG) application** built to demonstrate how large language models can answer questions from custom documents.

The app allows users to **upload a PDF**, ask questions about its content, and receive answers generated using **retrieved document context**.

The project is intentionally kept **simple, lightweight, and free** so it can be easily deployed on **Streamlit Community Cloud** and explained clearly in interviews.

---

## 🚀 Features

- Upload any PDF document
- Automatic text chunking and embedding
- Semantic search using FAISS
- Context-aware answer generation
- No paid APIs
- CPU-only (cloud friendly)
- Deployed using Streamlit

---

## 🧠 How RAG Works in This Project

This project follows a **classic RAG pipeline**:

### 1️⃣ Document Loading

- The uploaded PDF is loaded using `PyPDFLoader`.

### 2️⃣ Text Splitting

- The document is split into small overlapping chunks using `RecursiveCharacterTextSplitter`.
- This improves retrieval accuracy.

### 3️⃣ Embedding Generation

- Each chunk is converted into a vector embedding using:

### 4️⃣ Vector Storage (FAISS)

- All embeddings are stored in a FAISS vector database for fast similarity search.

### 5️⃣ Retrieval

- When a user asks a question, the most relevant document chunks are retrieved from FAISS.

### 6️⃣ Answer Generation

- The retrieved context is combined with the user’s question.
- A lightweight open-source language model (`google/flan-t5-small`) generates the final answer.

This approach ensures the model answers **based on the document**, not hallucinations.

---

## 🏗️ Project Structure

### 4️⃣ Vector Storage (FAISS)

- All embeddings are stored in a FAISS vector database for fast similarity search.

### 5️⃣ Retrieval

- When a user asks a question, the most relevant document chunks are retrieved from FAISS.

### 6️⃣ Answer Generation

- The retrieved context is combined with the user’s question.
- A lightweight open-source language model (`google/flan-t5-small`) generates the final answer.

This approach ensures the model answers **based on the document**, not hallucinations.

## 🖥️ Tech Stack

- **Python 3.10**
- **Streamlit** – UI and hosting
- **LangChain (community modules)** – document loading & embeddings
- **FAISS** – vector database
- **Sentence Transformers** – text embeddings
- **Hugging Face Transformers** – lightweight open-source LLM
- **PyPDF** – PDF parsing

---
