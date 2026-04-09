from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

with open("data.txt") as f:
    docs = [line.strip() for line in f.readlines()]
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(docs)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

def vector_search(query):
    q_emb = model.encode([query])
    D,I = index.search(np.array(q_emb),k=2)
    return [docs[i] for i in I[0]]
if __name__ == "__main__":
    query = "How does machine learning get dial?"
    print("Vector Search Results:")
    print(vector_search(query))