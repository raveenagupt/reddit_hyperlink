import networkx as nx
import csv
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_rows', None)  # Show all rows (None means no limit)


# Load your TSV file
df = pd.read_csv('soc-redditHyperlinks-body.tsv', sep='\t')  # Replace with your file path



df['LINK_SENTIMENT'] = pd.to_numeric(df['LINK_SENTIMENT'], errors='coerce')  # Convert sentiment to numeric if it's not already

# Count the occurrences of each post ID
post_id_counts = df['POST_ID'].value_counts()

# Group by 'post ID' and accumulate sentiment (e.g., sum of sentiment values)
post_sentiment = df.groupby('POST_ID')['LINK_SENTIMENT'].sum()

reddit_posts = df['TARGET_SUBREDDIT'].value_counts()

total_sentiment = df.groupby('TARGET_SUBREDDIT')['LINK_SENTIMENT'].sum()


# Merge the post ID counts and their accumulated sentiment into a single DataFrame
combined = pd.DataFrame({
    'count': post_id_counts,
    'sentiment': post_sentiment
})
combined2 = pd.DataFrame({
    'count': reddit_posts,
    'sentiment': total_sentiment
})
# Sort by the count of post IDs (highest first) and print the top 10
sorted_combined = combined.sort_values(by='count', ascending=False)
filtered_combined = sorted_combined.head(10)
sorted_combined2 = combined2.sort_values(by='count', ascending=False)
filtered_combined2 = sorted_combined2.head(100)

# Calculate the ratio of total sentiment to reddit posts count
combined2['sentiment_per_post'] = filtered_combined2['sentiment'] / filtered_combined2['count']

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(combined2.index, combined2['sentiment_per_post'], marker='o', linestyle='-', color='b')

# Adding labels and title
plt.xlabel('Ranking (1-100)', fontsize=12)
plt.ylabel('Sentiment to Posts Ratio', fontsize=12)
plt.title('Sentiment to Posts Ratio for Top 100 SubReddit', fontsize=14)

# Show the plot
plt.show()

#sorted_sentiment = total_sentiment.sort_values(ascending=False)
#sorted_sentiment_top10 = sorted_sentiment.head(10)



print(filtered_combined2)
#print(sorted_sentiment_top10)

#print(reddit_posts)
# Show the top 10 post IDs with their sentiment values
#print(sorted_combined.head(100))

'''
# Make sure your 'post ID' column is named correctly; adjust the name if needed
highest_post_ids = df['POST_ID'].value_counts()  # Change 10 to however many you want
top_post_ids = highest_post_ids.head(20)
print(top_post_ids)


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
'''
