import networkx as nx
G= nx.Graph()
G.add_edge("Python","Machine learning")
G.add_edge("Machine learning","Data")
G.add_edge("Data","Sensors")
G.add_edge("Sensors","IOT")
G.add_edge("IOT","Real-time data")
G.add_edge("Real-time data","Analytics")
G.add_edge("Analytics","Decision making")

def graph_rag(query):
    query = query.lower()
    if "machine learning" in query:
        return list(nx.bfs_edges(G,"Machine learning"))
    elif "data" in query:
        return list(nx.bfs_edges(G,"Data"))
    elif "sensors" in query:
        return list(nx.bfs_edges(G,"Sensors"))
    else:
        return "No relevant information found."
    neighbors = list(G.neighbors(node))
    context = []
    for n in neighbors:
        context.append(f"{node}->{n}")
        for n2 in G.neighbors(n):
            context.append(f"{n}->{n2}")
    return context
if __name__ == "__main__":
    query = "How does machine learning get data?"
    print("Graph RAG Results:")
    print(graph_rag(query))