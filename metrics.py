import csv
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns
import pandas as pd
import numpy as np
from networkx.algorithms.centrality import harmonic_centrality

# Create Graph
G = nx.DiGraph()

with open("datasets/soc-redditHyperlinks-body.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")
    next(tsv_file)
    for line in tsv_file:
        G.add_node(line[0]) #source subreddit
        G.add_node(line[1]) #dest subreddit
        G.add_edge(line[0], line[1], weight=line[4]) 

'''
# Metric Analysis on Individal nodes (subreddits)

# Betweenness Centrality
betweenness = nx.betweenness_centrality(G, normalized=True, endpoints=False)

# Betweenness Centrality Histogram
plt.figure(figsize=(10, 6))
sns.histplot(list(betweenness.values()), kde=False, bins=30)
plt.title('Betweenness Centrality Histogram')
plt.xlabel('Betweenness Centrality')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('histograms/node_betweenness_centrality_histogram.png')
plt.close()

# Save 100 largest and smallest betweenness centrality to CSV
betweenness_df = pd.DataFrame(list(betweenness.items()), columns=['Node', 'Betweenness Centrality'])
betweenness_df_sorted = betweenness_df.sort_values(by='Betweenness Centrality', ascending=False)
betweenness_df_sorted.head(100).to_csv('node_metrics_csvs/largest_betweenness.csv', index=False)
betweenness_df_sorted.tail(100).to_csv('node_metrics_csvs/smallest_betweenness.csv', index=False)



# Degree Centrality
degree = dict(G.degree())  # In-degree + Out-degree

# Degree Histogram
plt.figure(figsize=(10, 6))
sns.histplot(list(degree.values()), kde=False, bins=30)
plt.title('Degree Histogram')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('histograms/node_degree_histogram.png')
plt.close()

# Save 100 largest and smallest degrees to CSV
degree_df = pd.DataFrame(list(degree.items()), columns=['Node', 'Degree'])
degree_df_sorted = degree_df.sort_values(by='Degree', ascending=False)
degree_df_sorted.head(100).to_csv('node_metrics_csvs/largest_degree.csv', index=False)
degree_df_sorted.tail(100).to_csv('node_metrics_csvs/smallest_degree.csv', index=False)



# Clustering Coefficient
clustering = nx.clustering(G)

# Clustering Coefficient Histogram
plt.figure(figsize=(10, 6))
sns.histplot(list(clustering.values()), kde=False, bins=30)
plt.title('Clustering Coefficient Histogram')
plt.xlabel('Clustering Coefficient')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('histograms/node_clustering_coefficient_histogram.png')
plt.close()

# Save 100 largest and smallest clustering coefficients to CSV
clustering_df = pd.DataFrame(list(clustering.items()), columns=['Node', 'Clustering Coefficient'])
clustering_df_sorted = clustering_df.sort_values(by='Clustering Coefficient', ascending=False)
clustering_df_sorted.head(100).to_csv('node_metrics_csvs/largest_clustering_coefficient.csv', index=False)
clustering_df_sorted.tail(100).to_csv('node_metrics_csvs/smallest_clustering_coefficient.csv', index=False)

'''

# Harmonic Centrality
harmonics = harmonic_centrality(G)

# Harmonic Centrality Histogram
plt.figure(figsize=(10, 6))
sns.histplot(list(harmonics.values()), kde=False, bins=30)
plt.title('Harmonic Centrality Histogram')
plt.xlabel('Harmonic Centrality')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('histograms/node_harmonic_centrality_histogram.png')
plt.close()

# Save 100 largest and smallest harmonic centrality to CSV
harmonic_df = pd.DataFrame(list(harmonics.items()), columns=['Node', 'Harmonic Centrality'])
harmonic_df_sorted = harmonic_df.sort_values(by='Harmonic Centrality', ascending=False)
harmonic_df_sorted.head(100).to_csv('node_metrics_csvs/largest_harmonic.csv', index=False)
harmonic_df_sorted.tail(100).to_csv('node_metrics_csvs/smallest_harmonic.csv', index=False)


# PageRank
pagerank = nx.pagerank(G)

# PageRank Histogram
plt.figure(figsize=(10, 6))
sns.histplot(list(pagerank.values()), kde=False, bins=30)
plt.title('PageRank Histogram')
plt.xlabel('PageRank')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('histograms/node_pagerank_centrality_histogram.png')
plt.close()

# Save 100 largest and smallest PageRank to CSV
pagerank_df = pd.DataFrame(list(pagerank.items()), columns=['Node', 'PageRank'])
pagerank_df_sorted = pagerank_df.sort_values(by='PageRank', ascending=False)
pagerank_df_sorted.head(100).to_csv('node_metrics_csvs/largest_pagerank.csv', index=False)
pagerank_df_sorted.tail(100).to_csv('node_metrics_csvs/smallest_pagerank.csv', index=False)


'''

# Metric Analysis on communities

# Load community data csv
community_df = pd.read_csv("community_datasets/community_assignments_with_degree.csv", header=None, names=["node", "community", "degree_in", "degree_out"], skiprows=[0, 1])
node_community = dict(zip(community_df['node'], community_df['community']))



# Average Path Length
def average_path_length_per_community(G, node_community):
    communities = set(node_community.values())
    avg_path_lengths = {}

    for community in communities:
        subgraph_nodes = [node for node, comm in node_community.items() if comm == community]
        subgraph = G.subgraph(subgraph_nodes)

        # Calculate the average path length of the subgraph
        if len(subgraph) > 1:
            try:
                avg_length = nx.average_shortest_path_length(subgraph)
            except nx.NetworkXError:  # Handle non-strongly connected components
                # If the subgraph is not strongly connected, calculate on each SCC
                sccs = list(nx.strongly_connected_components(subgraph))
                avg_length = np.mean([nx.average_shortest_path_length(subgraph.subgraph(scc)) for scc in sccs])
        else:
            avg_length = 0  # Single-node subgraphs have no path length
        avg_path_lengths[community] = avg_length

    return avg_path_lengths

avg_path_lengths = average_path_length_per_community(G, node_community)

# Plot histogram for average path length
plt.figure()
plt.hist(list(avg_path_lengths.values()), bins=30, edgecolor='black')
plt.title('Average Path Length per Community')
plt.xlabel('Average Path Length')
plt.ylabel('# of Communities with Average Path Length')
plt.savefig('histograms/community_average_path_length_histogram.png')
plt.close()

# Get the top and bottom 10 communities by average path length
sorted_avg_path_lengths = sorted(avg_path_lengths.items(), key=lambda x: x[1], reverse=True)
top_100_avg_path_lengths = sorted_avg_path_lengths[:100]
#bottom_10_avg_path_lengths = sorted_avg_path_lengths[-10:]

# Save to CSV
with open('community_metrics_csvs/average_path_length.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Community", "Average Path Length"])
    for comm, length in top_100_avg_path_lengths:
        writer.writerow([comm, length])




# Clustering Coefficient per Community
def clustering_coefficient_per_community(G, node_community):
    communities = set(node_community.values())
    clustering_coeffs = {}

    for community in communities:
        subgraph_nodes = [node for node, comm in node_community.items() if comm == community]
        subgraph = G.subgraph(subgraph_nodes)

        # Calculate the average clustering coefficient of the subgraph
        clustering_coeff = nx.average_clustering(subgraph)
        clustering_coeffs[community] = clustering_coeff

    return clustering_coeffs

clustering_coeffs = clustering_coefficient_per_community(G, node_community)

# Plot histogram for clustering coefficient
plt.figure()
plt.hist(list(clustering_coeffs.values()), bins=30, edgecolor='black')
plt.title('Clustering Coefficient per Community')
plt.xlabel('Clustering Coefficient')
plt.ylabel('# of Communities with Clustering Coefficient')
plt.savefig('histograms/community_clustering_coefficient_histogram.png')
plt.close()

# Get the top and bottom 10 communities by clustering coefficient
sorted_clustering_coeffs = sorted(clustering_coeffs.items(), key=lambda x: x[1], reverse=True)
top_100_clustering_coeffs = sorted_clustering_coeffs[:100]
#bottom_10_clustering_coeffs = sorted_clustering_coeffs[-10:]

# Save to CSV
with open('community_metrics_csvs/clustering_coefficient.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Community", "Clustering Coefficient"])
    for comm, coeff in top_100_clustering_coeffs:
        writer.writerow([comm, coeff])




# Density per Community
def density_per_community(G, node_community):
    communities = set(node_community.values())
    densities = {}

    for community in communities:
        subgraph_nodes = [node for node, comm in node_community.items() if comm == community]
        subgraph = G.subgraph(subgraph_nodes)

        # Calculate the density of the subgraph
        density = nx.density(subgraph)
        densities[community] = density

    return densities

densities = density_per_community(G, node_community)

# Plot histogram for density
plt.figure()
plt.hist(list(densities.values()), bins=30, edgecolor='black')
plt.title('Density per Community')
plt.xlabel('Density')
plt.ylabel('# of Communities with Density')
plt.savefig('histograms/community_density_histogram.png')
plt.close()

# Get the top and bottom 10 communities by density
sorted_densities = sorted(densities.items(), key=lambda x: x[1], reverse=True)
top_100_densities = sorted_densities[:100]
#bottom_10_densities = sorted_densities[-10:]

# Save to CSV
with open('community_metrics_csvs/density.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Community", "Density"])
    for comm, density in top_100_densities:
        writer.writerow([comm, density])




# Average Degree per Community
def average_degree_per_community(G, node_community):
    communities = set(node_community.values())
    avg_degrees = {}

    for community in communities:
        subgraph_nodes = [node for node, comm in node_community.items() if comm == community]
        subgraph = G.subgraph(subgraph_nodes)

        # Calculate the average degree of the subgraph
        avg_degree = sum(dict(subgraph.degree()).values()) / len(subgraph)
        avg_degrees[community] = avg_degree

    return avg_degrees

avg_degrees = average_degree_per_community(G, node_community)

# Plot histogram for average degree
plt.figure()
plt.hist(list(avg_degrees.values()), bins=30, edgecolor='black')
plt.title('Average Degree per Community')
plt.xlabel('Average Degree')
plt.ylabel('# of Communities with Average Degree')
plt.savefig('histograms/community_average_degree_histogram.png')
plt.close()

# Get the top and bottom 10 communities by average degree
sorted_avg_degrees = sorted(avg_degrees.items(), key=lambda x: x[1], reverse=True)
top_100_avg_degrees = sorted_avg_degrees[:100]
#bottom_10_avg_degrees = sorted_avg_degrees[-10:]

# Save to CSV
with open('community_metrics_csvs/average_degree.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Community", "Average Degree"])
    for comm, degree in top_100_avg_degrees:
        writer.writerow([comm, degree])




# Edge Connectivity per Community
def edge_connectivity_per_community(G, node_community):
    communities = set(node_community.values())
    edge_connectivities = {}

    for community in communities:
        subgraph_nodes = [node for node, comm in node_community.items() if comm == community]
        subgraph = G.subgraph(subgraph_nodes)

        # Calculate the edge connectivity of the subgraph
        if len(subgraph) > 1:
            edge_connectivity = nx.edge_connectivity(subgraph)
        else:
            edge_connectivity = 0  # Single-node subgraphs have no edge connectivity
        edge_connectivities[community] = edge_connectivity

    return edge_connectivities

edge_connectivities = edge_connectivity_per_community(G, node_community)

# Plot histogram for edge connectivity
plt.figure()
plt.hist(list(edge_connectivities.values()), bins=30, edgecolor='black')
plt.title('Edge Connectivity per Community')
plt.xlabel('Edge Connectivity')
plt.ylabel('# of Communities with Edge Connectivity')
plt.savefig('histograms/community_edge_connectivity_histogram.png')
plt.close()

# Get the top and bottom 10 communities by edge connectivity
sorted_edge_connectivities = sorted(edge_connectivities.items(), key=lambda x: x[1], reverse=True)
top_100_edge_connectivities = sorted_edge_connectivities[:100]
#bottom_10_edge_connectivities = sorted_edge_connectivities[-10:]

# Save to CSV
with open('community_metrics_csvs/edge_connectivity.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Community", "Edge Connectivity"])
    for comm, conn in top_100_edge_connectivities:
        writer.writerow([comm, conn])




# Node Connectivity per Community
def node_connectivity_per_community(G, node_community):
    communities = set(node_community.values())
    node_connectivities = {}

    for community in communities:
        subgraph_nodes = [node for node, comm in node_community.items() if comm == community]
        subgraph = G.subgraph(subgraph_nodes)

        # Calculate the node connectivity of the subgraph
        if len(subgraph) > 1:
            node_connectivity = nx.node_connectivity(subgraph)
        else:
            node_connectivity = 0  # Single-node subgraphs have no node connectivity
        node_connectivities[community] = node_connectivity

    return node_connectivities

node_connectivities = node_connectivity_per_community(G, node_community)

# Plot histogram for node connectivity
plt.figure()
plt.hist(list(node_connectivities.values()), bins=30, edgecolor='black')
plt.title('Node Connectivity per Community')
plt.xlabel('Node Connectivity')
plt.ylabel('# of Communities with Node Connectivity')
plt.savefig('histograms/node_connectivity_histogram.png')
plt.close()

# Get the top and bottom 10 communities by node connectivity
sorted_node_connectivities = sorted(node_connectivities.items(), key=lambda x: x[1], reverse=True)
top_100_node_connectivities = sorted_node_connectivities[:100]
#bottom_10_node_connectivities = sorted_node_connectivities[-10:]

# Save to CSV
with open('community_metrics_csvs/node_connectivity.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Community", "Node Connectivity"])
    for comm, conn in top_100_node_connectivities:
        writer.writerow([comm, conn])

'''