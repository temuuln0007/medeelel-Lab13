import networkx as nx
import os

def read_net(filename):
    g = nx.Graph()

    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")

    with open(filename, encoding="utf-8") as f:
        f.readline()  # Skip the first line
        for l in f:
            nodes = l.strip().split(",")
            if len(nodes) >= 2:
                g.add_edge(nodes[0], nodes[1])  # Add an edge between two nodes
    return g

if __name__ == "__main__":
    # 📌 File paths (relative to project root)
    edge_file = r"data/asoiaf-all-edges.csv"
    node_file = r"data/asoiaf-all-nodes.csv"

    print(f"Checking if files exist at:\n{edge_file}\n{node_file}")
    if not os.path.exists(edge_file):
        print(f"Edge file not found at: {edge_file}")
    if not os.path.exists(node_file):
        print(f"Node file not found at: {node_file}")
    if not os.path.exists(edge_file) or not os.path.exists(node_file):
        raise FileNotFoundError("One or more files are missing!")

    # Read edge file
    g = read_net(edge_file)

    # Add node information (house)
    with open(node_file, encoding="utf-8") as f:
        f.readline()  # Skip the first line
        for l in f:
            parts = l.rstrip().split(",")
            if len(parts) >= 3:
                node, _, house = parts
                g.add_node(node, house=house)

    # Layout (for future visualization use)
    pos = nx.spring_layout(g)

    # Summary
    print("✅ Graph created successfully!")
    print(f"🔢 Total nodes: {g.number_of_nodes()}")
    print(f"🔗 Total edges: {g.number_of_edges()}")

    # Optional: Save the graph object for reuse
    nx.write_gml(g, "results/asoiaf-network.gml")
    print("📁 Graph saved to results/asoiaf-network.gml")
