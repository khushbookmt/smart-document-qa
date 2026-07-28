import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

# Import our own functions
from utils.pdf_reader import extract_pdf_text
from utils.chunking import split_text
# ----------------------------------
# Load API Key
# ----------------------------------
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found.")

print("API Key Loaded Successfully")
print("Key Prefix:", api_key[:6])

# ----------------------------------
# Create Gemini Client
# ----------------------------------
client = genai.Client(api_key=api_key)

print("Gemini Client Created Successfully")

# ----------------------------------
# Read PDF
# ----------------------------------
text = extract_pdf_text("sample.pdf")
chunks = split_text(text)

# ----------------------------------
# Generate Embeddings
# ----------------------------------

print("\nGenerating Embeddings...\n")

print("\nGenerating Embeddings...")

response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=chunks
)

embeddings = [embedding.values for embedding in response.embeddings]

print("\nEmbeddings Generated Successfully!")

print(f"Total Embeddings: {len(embeddings)}")
print(f"Embedding Dimension: {len(embeddings[0])}")
