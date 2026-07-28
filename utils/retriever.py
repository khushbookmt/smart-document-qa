import numpy as np

def retrieve_chunks(index,query_embedding,chunks,k=3):
   
 query_embedding = np.array([query_embedding]).astype('float32')
 distances,indices = index.search(query_embedding,k)
 retrieved_chunks = [chunks[i] for i in indices[0]]
 return retrieved_chunks
    