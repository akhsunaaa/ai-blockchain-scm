import networkx as nx

# Create a graph
G = nx.Graph()

# Define nodes (warehouses, suppliers, customers)
locations = ["Warehouse", "Supplier A", "Supplier B", "Customer A", "Customer B"]
edges = [
    ("Warehouse", "Supplier A", 10),
    ("Warehouse", "Supplier B", 15),
    ("Supplier A", "Customer A", 25),
    ("Supplier B", "Customer B", 30),
    ("Supplier A", "Supplier B", 5),
    ("Customer A", "Customer B", 10)
]

# Add edges with weights (distance)
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Find shortest path from Warehouse to Customers
shortest_path = nx.shortest_path(G, source="Warehouse", target="Customer A", weight="weight")

print("Optimal Route:", shortest_path)
