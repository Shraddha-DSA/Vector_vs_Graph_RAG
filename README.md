# Vecor Vs Graph RAG
This project demonstrates the difference between **Vector Database(Semantic Retrieval)** and **Graph RAG(Hierarchical Retrieval)** using a simple data.
The goal is to understand:
- How semantic search works using embeddings
- How Graph RAG performs multi-hop reasoning
- When to use each approach
- How they complement each other

---
## What is Vector RAG?
Vector RAG retrieves information based on **semantic similarity**.

Text is converted into embeddings and stored in a vector database. Queries are also embedded and matched using similarity search.

It finds **similar meaning**, but does not reason.

## What is Graph RAG?
Graph RAG retrieves information using **relationships between entities**.

Data is stored as a graph

This enables **multi-hop reasoning**.
