import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

from utils.pdf_reader import extract_pdf_text
from utils.chunking import split_text
from utils.embedding import generate_embeddings
from utils.vector_store import create_vector_store
from utils.storage import save_vector_store

# ------------------------
# Load API Key
# ------------------------
print("Step 7 started")

load_dotenv(Path(__file__).parent / ".env")

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

print("Gemini Client Ready")

# ------------------------
# Read PDF
# ------------------------

print("\nReading PDF...")

text = extract_pdf_text("sample.pdf")

# ------------------------
# Split into Chunks
# ------------------------

chunks = split_text(text)

print(f"Total Chunks : {len(chunks)}")

# ------------------------
# Generate Embeddings
# ------------------------

print("\nGenerating Embeddings...")

embeddings = generate_embeddings(client, chunks)

print(f"Embeddings Generated : {len(embeddings)}")

# ------------------------
# Create Vector Store
# ------------------------

index = create_vector_store(embeddings)

print("FAISS Index Created")

# ------------------------
# Save Everything
# ------------------------

save_vector_store(index, chunks)

print("\nVector Store Saved Successfully!")

print("Files Created:")
print("data/index.faiss")
print("data/chunks.pkl")