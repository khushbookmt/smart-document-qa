import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

from utils.storage import load_vector_store
from utils.embedding import generate_embeddings
from utils.retriever import retrieve_chunks
from utils.llm import generate_answer

# ------------------------
# Load Environment Variables
# ------------------------

env_path = Path(__file__).parent / ".env"

load_dotenv(env_path)

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

print("Gemini Client Ready!")

# ------------------------
# Load Saved Vector Store
# ------------------------

print("\nLoading Vector Database...")

index, chunks = load_vector_store()

print("Vector Database Loaded Successfully!")
print(f"Total Chunks : {len(chunks)}")
print(f"Total Vectors : {index.ntotal}")

# ------------------------
# Chat Loop
# ------------------------

while True:

    question = input("\nAsk your question (type 'exit' to quit): ")

    if question.lower() in ("exit",'quit','q'):
        print("\nGoodbye!")
        break

    # Generate query embedding
    query_embedding = generate_embeddings(
        client,
        [question]
    )[0]

    # Retrieve relevant chunks
    retrieved_chunks = retrieve_chunks(
        index,
        query_embedding,
        chunks,
        k=3
    )

    # Create context
    context = "\n\n".join(retrieved_chunks)

    # Generate answer
    answer = generate_answer(
        client,
        context,
        question
    )

    print("\n" + "=" * 60)
    print("ANSWER")
    print("=" * 60)

    print(answer)