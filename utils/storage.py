import pickle
import faiss
import os

def save_vector_store(index,chunks):
    os.makedirs('data',exist_ok=True)
    faiss.write_index(index,'data/index.faiss')
    with open('data/chunks.pkl','wb') as file:
        pickle.dump(chunks,file)


def load_vector_store():
    index = faiss.read_index('data/index.faiss')
    with open('data/chunks.pkl','rb') as file:
        chunks = pickle.load(file)

    return index, chunks 