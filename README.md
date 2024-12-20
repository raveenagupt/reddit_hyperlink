# reddit_hyperlink
Network In the Real World Project

Purpose: Research shows that subreddits influence each other's popularity through community and hyperlink interactions. This project analyzes the dynamics that make subreddits influential by exploring community structures, sentiment, post properties and growth patterns. Our team uses network metrics like degree centrality, clustering coefficient, logistic regression, and “epidemic” simulations to identify key trends, such as the “rich getting richer” phenomena, where popular subreddits amplify their reach by reposting content from other large subreddits. Community detection also reveals how specific clusters can contribute to visibility, and how for certain content to go viral, it must bridge multiple communities. Sentiment analysis depicts that positive sentiment drives more growth and influence than negative sentiment. Additionally, in-degree centrality, where one subreddit is hyperlinked by another, increases “popularity” more than out-degree. By identifying these factors, our project provides insights into strategies that can help subreddits and its respective content gain virality. 

Run "pip install requirements.txt" to install all necessary python libraries

**some things were removed for gradescope submission because it wouldn't accept this much

Python files:
- community_clusters.py: maps communities
- detect_community.py: performs a community detection algorithm and creates a CSV with communities
- ExpectedIncrease.py: runs an algorithm to find how much of an influence getting hyperlinked by a hub can affect a niche subreddit
- find_high_comm.py: goes through the community_metrics CSVs and prints which communities appear at the top of the most metrics
- HighestDegrees.py: generates degree over time for some highest rank subreddits
- influential_nodes.py: takes in the resulting CSV of detect_community.py and extracts the top nodes of each community
- metrics.py: finds the top and bottom 10 nodes/commmunities for each metric then makes a histogram for each metric
- MiddleDegree.py: generates degree over time for some middle rank subreddits
- out_communities_nodes.py: display the nodes with the highest out edges to different communities 
- post_properties.py: performs logistic regression to determine which post properties have the most influence on a post being popular
- reddit.py: finds metrics like giant component and average degree of the graphs as a whole and makes degree distribution plots
- Sentiment.py: graphs top 100 subreddit sentiment ratios
- SI_giant_component: removes giant component for SI.py
- SI.py: treats the network like an epidemic and uses and SI model to determine spread of information (v1)
- SIModel.py: treats the network like an epidemic and uses and SI model to determine spread of information (v2)
- visualize.py: visualizes the graph as a whole
- TimeToGiant.py: loops through subreddits from the SI model and graphs the time evolution

Results directories
- community_datasets: CSVs that show which subreddit is in which community that were created in detect_comunity.py
- community_metrics_csvs: CSVs that show the top and bottom 10 communities for each metric that were created in metric.py
- datasets (might not be in the repository since it is too large to add to github): original datasets downloaded from https://snap.stanford.edu/data/soc-RedditHyperlinks.html
- graph_edges.csv: csv of just the source and destination node of each edge
- histograms: histograms saved in metrics.py of the distribution of each node metric and community metric
- node_metrics_csvs: SVs that show the top and bottom 10 nodes for each metric that were created in metric.py
- post_properties_results: histograms of post property distributions and bar plot of the influence of each post proeprty generated in post_properties.py
- subredit_sentiment.csv: compiles the sentiments of each subreddit