import csv
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.DiGraph()

with open("datasets/soc-redditHyperlinks-body.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")
    next(tsv_file)
    for line in tsv_file:
        G.add_node(line[0]) #source subreddit
        G.add_node(line[1]) #dest subreddit
        G.add_edge(line[0], line[1], weight=line[4]) 

with open("datasets/soc-redditHyperlinks-title.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")
    next(tsv_file)
    for line in tsv_file:
        G.add_node(line[0]) #source subreddit
        G.add_node(line[1]) #dest subreddit
        G.add_edge(line[0], line[1], weight=line[4])

connected_components = list(nx.strongly_connected_components(G))
giant_component = max(connected_components, key=len)
G_giant = G.subgraph(giant_component)
print(f"Giant component has {G_giant.number_of_nodes()} nodes and {G_giant.number_of_edges()} edges.")

#avg_path_length = nx.average_shortest_path_length(G_giant)
diameter = nx.diameter(G_giant)
avg_clustering = nx.average_clustering(G_giant)
global_cluster = nx.transitivity(G_giant)

sum_degree = sum(dict(G_giant.degree()).values())
avg_degree = sum_degree/G_giant.number_of_nodes()

#print(f"The average path length is {avg_path_length}")
print(f"The diameter is {diameter}")
print(f"The avg clustering is {avg_clustering}")
print(f"The global clustering is {global_cluster}")
print(f"The average degree is {avg_degree}")




degree_list = []
degree_occ = {}  
for node, degree in G.degree():
    degree_list.append(degree)

degree_list.sort()

for degree in degree_list:
    if degree in degree_occ:
        degree_occ[degree] += 1
    else:
        degree_occ[degree] = 1

sorted_degrees = sorted(degree_occ.keys())  
total_nodes = G.number_of_nodes()

probability = []  

for degree in sorted_degrees:
    probability.append(degree_occ[degree] / total_nodes)  


plt.figure(figsize=(10, 10))
plt.plot(sorted_degrees, probability, 'bo', markersize=4)
plt.title('Degree Distribution in Linear Scale FIRST GRAPH')
plt.xlabel('Degree (k)')
plt.ylabel('P(degree = k)')
plt.grid(True)
plt.show()


plt.figure(figsize=(10, 10))
plt.loglog(sorted_degrees, probability, 'bo', markersize=4) 
plt.title('Degree Distribution in Log-Log Scale SECOND GRAPH')
plt.xlabel('Degree (k)')
plt.ylabel('P(degree = k)')
plt.grid(True)
plt.show()




bins = np.logspace(0, np.log10(max(degree_list)), 50) 
widths = bins[1:] - bins[:-1]  


hist, _ = np.histogram(degree_list, bins=bins, density=False)
hist_norm = hist / widths  

plt.figure(figsize=(10, 6))
plt.scatter(bins[:-1], hist_norm, alpha=0.7)  
plt.xscale('log')
plt.yscale('log')
plt.title('Degree Distribution in Log-Log Scale with Logarithmic Binning THIRD GRAPH')
plt.xlabel('Degree (k)')
plt.ylabel('Normalized Count')
plt.grid(True)
plt.show()


reversed_prob = list(reversed(probability))  
ccdf = np.cumsum(reversed_prob)  
ccdf = list(reversed(ccdf))  #
plt.figure(figsize=(10, 6))
plt.loglog(sorted_degrees, ccdf, 'bo',markersize=4)  
plt.title('CCDF: P(degree > k) in Log-Log Scale FOURTH GRAPH')
plt.xlabel('Degree (k)')
plt.ylabel('P(degree > k)')
plt.grid(True)
plt.show()

