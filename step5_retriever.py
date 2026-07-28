import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

from utils.pdf_reader import extract_pdf_text
from utils.chunking import split_text
from utils.vector_store import create_vector_store
from utils.retriever import retrieve_chunks
from utils.embedding import (generate_embeddings ,generate_query_embedding)

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
print(type(embeddings))
print(type(embeddings[0]))
print(len(embeddings[0]))

# ------------------------
# Create FAISS Index
# ------------------------
index = create_vector_store(embeddings)
print('Faiss Index Ready!')

# ------------------------
# User Question
# ------------------------
query = input("\nAsk your question: ")

# ------------------------
# Query Embedding
# ------------------------
query_embedding = generate_query_embedding(client,query)
# ------------------------
# Retrieve Chunks
# ------------------------
results = retrieve_chunks(index,query_embedding,chunks,k=3)
print("\nTop Matching Chunks\n")

for i, chunk in enumerate(results, start=1):
    print("=" * 60)
    print(f"Chunk {i}")
    print("=" * 60)
    print(chunk)
    print()
