import networkx as nx
import community as community_louvain
import csv
import matplotlib.pyplot as plt

# Create the graph (directed)
G = nx.DiGraph()

# Load the graph data
with open("datasets/soc-redditHyperlinks-body.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")
    next(tsv_file)  # Skip header
    for line in tsv_file:
        G.add_node(line[0])  # source subreddit
        G.add_node(line[1])  # destination subreddit
        G.add_edge(line[0], line[1])  # add edge

# Detect communities using Louvain (convert to undirected graph for community detection)
partition = community_louvain.best_partition(G.to_undirected())

# Save community assignments along with in-degree and out-degree to CSV
with open("community_assignments_with_degree.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Subreddit", "Community", "In-Degree", "Out-Degree"])  # Column headers
    
    for node in G.nodes():
        in_degree = G.in_degree(node)
        out_degree = G.out_degree(node)
        writer.writerow([node, partition[node], in_degree, out_degree])  # Write data for each node

# Visualize the communities
colors = [partition[node] for node in G.nodes()]
pos = nx.spring_layout(G)  # Use spring layout for better positioning
plt.figure(figsize=(12, 12))
nx.draw(G, pos, node_color=colors, with_labels=True, node_size=50, font_size=10, cmap=plt.cm.jet)
plt.show()

print("Community detection and degree calculation complete. Data saved to 'community_assignments_with_degree.csv'.")
