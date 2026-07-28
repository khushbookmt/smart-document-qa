import faiss
import numpy as np
def create_vector_store(embeddings):
    """
    Create a FAISS index from embedding vectors.

    Args:
        embeddings (list): List of embedding vectors.

    Returns:
        faiss.IndexFlatL2
    """
    embeddings = np.array(embeddings).astype('float32')
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index