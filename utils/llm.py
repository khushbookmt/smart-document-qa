def generate_answer(client,context,question):
    prompt = f"""You are a helpful AI assistant.

Answer the question ONLY from the provided context.

If the answer is not present in the context, reply:

"I couldn't find the answer in the provided document."

------------------------
Context:

{context}

------------------------
Question:
{question}

Answer:
"""
    response = client.models.generate_content(
        model ='gemini-flash-latest',
        contents = prompt)

    return response.text