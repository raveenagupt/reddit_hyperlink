import pandas as pd
from collections import defaultdict

# Load community assignments
community_assignments = pd.read_csv("community_assignments.csv", header=None, names=["node", "community"])
node_to_community = dict(zip(community_assignments["node"], community_assignments["community"]))

# Load graph edges
graph_edges = pd.read_csv("graph_edges.csv", header=None, names=["source", "target"])

# Calculate bridges and degrees
bridge_degrees = defaultdict(int)

for _, row in graph_edges.iterrows():
    source, target = row["source"], row["target"]
    source_comm = node_to_community.get(source)
    target_comm = node_to_community.get(target)
    
    # Check if this is a bridge (connects different communities)
    if source_comm != target_comm:
        bridge_degrees[source] += 1
        bridge_degrees[target] += 1

# Sort nodes by degree
sorted_bridges = sorted(bridge_degrees.items(), key=lambda x: x[1], reverse=True)

# Display top bridges
print("Top bridges and their degrees:")
for node, degree in sorted_bridges[:10]:
    print(f"Node: {node}, Degree to other communities: {degree}")
