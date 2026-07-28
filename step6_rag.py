import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

from utils.pdf_reader import extract_pdf_text
from utils.chunking import split_text
from utils.embedding import (
    generate_embeddings,
    generate_query_embedding
)
from utils.vector_store import create_vector_store
from utils.retriever import retrieve_chunks
from utils.llm import generate_answer

# ------------------------
# Load API Key
# -----------------------
env_path = Path(__file__).parent / ".env"
loaded = load_dotenv(dotenv_path=env_path, override=True)
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)
print("Gemini Client Created Successfully")
# ------------------------
# Read PDF and chunks
# ------------------------
text = extract_pdf_text('sample.pdf')
chunks = split_text(text)
print("Total Chunks :", len(chunks))

# ------------------------
# Create Embeddings
# ------------------------
print("Generating Embeddings...")

embeddings = generate_embeddings(client,chunks)

print(f"Embeddings Generated : {len(embeddings)}")

# ------------------------
# Create FAISS Index
# ------------------------
index = create_vector_store(embeddings)
print('Faiss Index Ready!')

query = input("\nAsk your question: ")

query_embedding = generate_query_embedding(client,query)


#retrieve chunks
retrieved_chunks = retrieve_chunks(
    index,
    query_embedding,
    chunks,
    k=3
)

context = "\n\n".join(retrieved_chunks)

answer = generate_answer(
    client,
    context,
    query
)

print("\n" + "=" * 60)
print("ANSWER")
print("=" * 60)

print(answer)