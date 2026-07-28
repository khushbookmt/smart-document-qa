def generate_embeddings(client,texts):
    if not texts:
        raise ValueError('Text list is empty')
    response = client.models.embed_content(
        model = "gemini-embedding-001",
        contents = texts
    )
    return [embedding.values for embedding in response.embeddings]


def generate_query_embedding(client,query):
    response = client.models.embed_content(
        model = 'gemini-embedding-001',
        contents = query
    )

    return response.embeddings[0].values