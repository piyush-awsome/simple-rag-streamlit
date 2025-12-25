from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from transformers import pipeline


def create_vectorstore(pdf_path):
    # Load PDF
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    # Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(docs)

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore


def answer_question(vectorstore, question):
    # Retrieve relevant chunks
    docs = vectorstore.similarity_search(question, k=1)
    context = "\n".join([d.page_content for d in docs])

    # Simple free model
    generator = pipeline(
        "text2text-generation",
        model="google/flan-t5-small",
        max_new_tokens=200
    )

    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {question}
    """

    result = generator(prompt)
    return result[0]["generated_text"]
