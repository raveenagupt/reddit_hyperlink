import networkx as nx
import csv
import random
import matplotlib.pyplot as plt

# Load graph edges (directed graph)
G = nx.DiGraph()

# Load the graph data
with open("graph_edges.csv") as file:
    tsv_file = csv.reader(file, delimiter=",")
    for line in tsv_file:
        G.add_edge(line[0], line[1])  # Add edge (source, target)

# Load community assignments
community_assignments = {}
with open("community_assignments.csv") as file:
    tsv_file = csv.reader(file, delimiter=",")
    next(tsv_file)  # Skip the header row
    for line in tsv_file:
        community_assignments[line[0]] = int(line[1])  # Map subreddit to community

# Function to simulate the infection spread
def spread_infection(initial_infected_nodes, G, community_assignments, steps=10):
    infected = set(initial_infected_nodes)  # Set of initially infected nodes
    infected_over_time = [len(infected)]  # Track infected nodes per step

    # Define probabilities
    in_community_prob = 0.2  # Higher probability for same community
    out_community_prob = 0.1  # Lower probability for different community

    # Simulation steps
    for step in range(steps):
        new_infected = set()
        for node in list(infected):
            # Look at the neighbors (outgoing edges from the current node)
            for neighbor in G.neighbors(node):
                if neighbor not in infected:
                    # Check if the neighbor is in the same community
                    if community_assignments.get(node) == community_assignments.get(neighbor):
                        if random.random() < in_community_prob:
                            new_infected.add(neighbor)
                    else:
                        if random.random() < out_community_prob:
                            new_infected.add(neighbor)
        
        # Add newly infected nodes to the infected set
        infected.update(new_infected)
        infected_over_time.append(len(infected))  # Track infected nodes count

        print(f"Step {step+1}: Infected nodes: {len(infected)}")

    return infected_over_time

# Example usage: infect multiple specific nodes (subreddits)
initial_infected_nodes = ["askreddit", "pcmasterrace"]  # Multiple seeds
infection_data = spread_infection(initial_infected_nodes, G, community_assignments)

# Plot infection spread over time
plt.figure(figsize=(10, 6))
plt.plot(range(len(infection_data)), infection_data, marker='o', linestyle='-')
plt.xlabel("Iteration")
plt.ylabel("Number of Infected Nodes")
plt.title(f"Infection Spread Over Time Starting from Seeds: {', '.join(initial_infected_nodes)}")
plt.grid(True)
plt.show()
