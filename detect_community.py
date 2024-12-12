import networkx as nx
import community as community_louvain
import csv
import matplotlib.pyplot as plt
from collections import Counter

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

# Save community assignments along with node information to CSV
with open('community_assignments.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Subreddit', 'Community'])  # Column headers
    for node in G.nodes():
        writer.writerow([node, partition[node]])  # Write node and its community assignment

# Save the graph edges to a CSV
with open('graph_edges.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Source', 'Target'])  # Column headers
    for edge in G.edges():
        writer.writerow(edge)  # Write source and target for each edge

# Get the size of each community
community_sizes = Counter(partition.values())

# Get the 10 largest communities (by number of subreddits)
top_10_communities = [community for community, size in community_sizes.most_common(10)]

# Filter the graph to only include nodes from the top 10 communities
filtered_nodes = [node for node in G.nodes() if partition[node] in top_10_communities]
filtered_graph = G.subgraph(filtered_nodes)

# Visualize the filtered graph (top 10 communities)
filtered_partition = {node: partition[node] for node in filtered_graph.nodes()}
colors = [filtered_partition[node] for node in filtered_graph.nodes()]
pos = nx.spring_layout(filtered_graph, k=0.15, iterations=20)  # Increase spacing between nodes

plt.figure(figsize=(12, 12))
nx.draw(filtered_graph, pos, node_color=colors, with_labels=False, node_size=0.5, font_size=10, cmap=plt.cm.jet)
plt.title("Top 10 Communities (Filtered)")
plt.show()

print("Community detection, graph edge saving, and community assignment complete.")
print("Data saved to 'community_assignments.csv' and 'graph_edges.csv'.")
