import os 
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from utils.pdf_reader import extract_pdf_text
from utils.chunking import split_text
from utils.vector_store import create_vector_store
from utils.embedding import generate_embeddings 
# ------------------------
# Load API Key
# ------------------------
env_path = Path(__file__).parent/'.env'
load_dotenv(env_path)

api_key = os.getenv('GOOGLE_API_KEY')
client = genai.Client(api_key=api_key)
print("Gemini Client Created Successfully")
# ------------------------
# Read PDF and split text
# ------------------------
text = extract_pdf_text('sample.pdf')
chunks =split_text(text)
print(f"Total Chunks : {len(chunks)}")
# ------------------------
# Generate Embeddings
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
print("FAISS Index Created Successfully")

print("Total Vectors :", index.ntotal)