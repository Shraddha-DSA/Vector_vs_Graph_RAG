from vector_search import vector_search
from graph_rag import graph_rag
query = "How does machine learning get data?"
print("Vector Search Results:")
print(vector_search(query))
print("\nGraph RAG Results:")
print(graph_rag(query))