import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('community_assignments_with_degree.csv')

# Calculate the total degree (In-Degree + Out-Degree)
df['Total_Degree'] = df['In-Degree'] + df['Out-Degree']

# Create a graph
G = nx.Graph()

# Add nodes with communities as attributes
for _, row in df.iterrows():
    G.add_node(row['Subreddit'], community=row['Community'], total_degree=row['Total_Degree'])

# Create edges within the same community
for community in df['Community'].unique():
    community_subreddits = df[df['Community'] == community]['Subreddit'].tolist()
    
    # Add edges between subreddits in the same community (fully connected within each community)
    for i in range(len(community_subreddits)):
        for j in range(i + 1, len(community_subreddits)):
            G.add_edge(community_subreddits[i], community_subreddits[j], color='gray')

# Extract top 10 nodes (subreddits) per community based on their total degree
top_nodes_per_community = df.sort_values(by=['Community', 'Total_Degree'], ascending=[True, False]) \
                            .groupby('Community').head(3)

# Get the top 10 nodes and assign them a 'highlighted' color
highlighted_nodes = top_nodes_per_community['Subreddit'].tolist()

# Assign colors based on the community
community_colors = {community: idx for idx, community in enumerate(df['Community'].unique())}
node_colors = [community_colors[G.nodes[node]['community']] for node in G.nodes]

# Extract edges' colors
edge_colors = [G[u][v]['color'] for u, v in G.edges]

# Plot the graph with edges colored gray
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, k=0.15, iterations=20)  # Use spring layout for better positioning
nx.draw(G, pos, node_size=50, node_color=node_colors, with_labels=True, font_size=10, cmap=plt.cm.jet, edge_color=edge_colors)

# Highlight the top 10 nodes with the highest degree in each community
nx.draw_networkx_nodes(G, pos, nodelist=highlighted_nodes, node_color='r', node_size=100)

# Show plot
plt.title('Subreddit Community Graph (Top 10 Nodes Highlighted)')
plt.show()
