
from google.genai import errors


def generate_answer(client, context, question):

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

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        return response.text or "I couldn't generate an answer. Please try again."

    except errors.ServerError as e:

        if getattr(e, "code", None) == 503:
            return (
                "Gemini is temporarily experiencing high demand. "
                "Your PDF is safe. Please wait a minute and try your question again."
            )

        return f"Gemini server error: {e}"

    except Exception as e:
        return f"An error occurred while generating your answer: {e}"
