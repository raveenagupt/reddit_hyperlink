import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random


def findInfectionTime(weight):
    if(weight >= 100):
        return 1
    ran = random.randint(-1,1)
    return 11 - (weight // 10) + ran


#df = pd.read_csv('test.tsv', sep='\t')
df = pd.read_csv('soc-redditHyperlinks-body.tsv', sep='\t')

G = nx.DiGraph()

for index, row in df.iterrows():
    source = row['SOURCE_SUBREDDIT']
    target = row['TARGET_SUBREDDIT']
    if(G.has_edge(source,target)):
        G[source][target]['weight'] += 1
        #G[source][target]['time'] = 5
    else:
        G.add_edge(source, target, weight=1)


# Set initial infected nodes (can be modified)
initial_infected = ['askreddit']  # Example of starting infected nodes

# Initialize node states: S = susceptible, I = infected
node_states = {node: 'S' for node in G.nodes}
for node in initial_infected:
    node_states[node] = 'I'

# Create a dictionary to store the time when nodes will become infected
infection_times = {node: -1 for node in G.nodes}

# Set the initial infected nodes to time 0
for node in initial_infected:
    infection_times[node] = 0

# Simulation parameters
max_timesteps = 100  # You can set this to any value based on your simulation needs
timesteps = 0

# List to track the number of infected nodes at each timestep
infected_counts = []
i = 0
# Run the SI model
while timesteps < max_timesteps:
    # Track the number of infected nodes at this timestep
    infected_count = sum(1 for state in node_states.values() if state == 'I')
    infected_counts.append(infected_count)

    # Go through each node to check for infection spread
    for node in G.nodes:
        if node_states[node] == 'I':
            # This node is infected, check its neighbors
            for neighbor in G.predecessors(node):
                if node_states[neighbor] == 'S' and infection_times[neighbor] == -1:
                    # Calculate the infection time based on the weight of the edge
                    edge_weight = G[neighbor][node]['weight']

                    if(infection_times[neighbor] == -1):
                        time_to_infect = findInfectionTime(edge_weight)
                    
                        # If the neighbor has not been infected earlier or can be infected now
                        infection_times[neighbor] = timesteps + time_to_infect

    # Increment timestep
    timesteps += 1
    
    # Update the node states based on the infection times
    for node in G.nodes:
        if node_states[node] == 'S' and infection_times[node] != -1 and infection_times[node] <= timesteps:
            node_states[node] = 'I'
            i += 1


    
print(i)

# Plotting the number of infected nodes over time
plt.plot(range(timesteps), infected_counts)
plt.xlabel('Timestep')
plt.ylabel('Number of Infected Nodes')
plt.title(f'Number of Infected Nodes Over Time with Seed as {initial_infected[0]}')
plt.grid(True)
plt.show()