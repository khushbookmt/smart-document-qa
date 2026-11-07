import os
import tempfile
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from google import genai

from utils.pdf_reader import extract_pdf_text
from utils.chunking import split_text
from utils.embedding import generate_embeddings
from utils.vector_store import create_vector_store
from utils.retriever import retrieve_chunks
from utils.llm import generate_answer

# =====================================================
# Load Gemini API
# =====================================================

env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# =====================================================
# Page Config
# =====================================================

st.set_page_config(
    page_title="Smart Document Q&A",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Smart Document Q&A")

# =====================================================
# Session State
# =====================================================

if "index" not in st.session_state:
    st.session_state.index = None

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "processed" not in st.session_state:
    st.session_state.processed = False

# =====================================================
# Layout
# =====================================================

left, right = st.columns([1, 3])

# =====================================================
# LEFT PANEL
# =====================================================

with left:

    st.subheader("📂 Upload PDFs")

    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        st.write("### Selected Files")

        for pdf in uploaded_files:
            st.write("📄", pdf.name)

    if st.button("🚀 Process PDFs", use_container_width=True):

        if not uploaded_files:
            st.warning("Please upload at least one PDF.")
            st.stop()

        all_text = ""

        progress = st.progress(0)

        for i, uploaded_file in enumerate(uploaded_files):

            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:

                tmp.write(uploaded_file.getbuffer())

                pdf_path = tmp.name

            text = extract_pdf_text(pdf_path)

            all_text += "\n\n" + text

            os.remove(pdf_path)

            progress.progress((i + 1) / len(uploaded_files))

        with st.spinner("Creating Knowledge Base..."):

            chunks = split_text(all_text)

            embeddings = generate_embeddings(client, chunks)

            index = create_vector_store(embeddings)

        st.session_state.index = index
        st.session_state.chunks = chunks
        st.session_state.processed = True

        st.success("Knowledge Base Ready!")

# =====================================================
# RIGHT PANEL
# =====================================================

with right:

    st.subheader("💬 Chat")

    question = st.text_input(
        "",
        placeholder="Ask anything about your PDFs..."
    )

    if st.button("Ask"):

        if not st.session_state.processed:

            st.warning("Please process your PDFs first.")

            st.stop()

        if question.strip() == "":

            st.warning("Please enter a question.")

            st.stop()

        with st.spinner("Searching..."):

            response = client.models.embed_content(
                model="gemini-embedding-001",
                contents=question
            )

            query_embedding = response.embeddings[0].values

            retrieved_chunks = retrieve_chunks(
                st.session_state.index,
                query_embedding,
                st.session_state.chunks,
                k=3
            )

            context = "\n\n".join(retrieved_chunks)

            answer = generate_answer(
                client,
                context,
                question
            )

        st.markdown("---")

        st.subheader("🤖 Answer")

        st.write(answer)