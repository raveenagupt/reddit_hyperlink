import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the CSV data
edges_df = pd.read_csv("graph_edges.csv")

# Clean column names: strip spaces and standardize case
edges_df.columns = edges_df.columns.str.strip().str.upper()  # Convert to upper case for uniformity

# Define subreddits of interest
selected_subreddits = {'videos','youtube'}  # Set for quick lookup

# Filter edges that involve any of the selected subreddits
filtered_df = edges_df[
    edges_df['SOURCE'].isin(selected_subreddits) | edges_df['TARGET'].isin(selected_subreddits)
]

# Create a directed graph from the filtered data
G = nx.from_pandas_edgelist(filtered_df, source='SOURCE', target='TARGET', create_using=nx.DiGraph())

# Draw the subgraph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, k=0.3)  # Layout for better visualization
nx.draw(G, pos, with_labels=True, node_size=3, node_color="skyblue", font_size=5, font_weight="bold", edge_color="gray")
plt.title("Network Visualization of Selected Subreddits: AskReddit, pics, videos")
plt.show()
