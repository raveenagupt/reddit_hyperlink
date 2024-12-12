import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load community data
data = pd.read_csv('community_assignments_with_degree.csv')

# Pivot data so each row represents a community and columns represent subreddits
community_data = data.pivot_table(index='Community', columns='Subreddit', values='In-Degree', aggfunc='first')

# Create the heatmap
plt.figure(figsize=(14, 8))
sns.heatmap(community_data, cmap="Set1", cbar=False, linewidths=0.5, square=True)

# Title and labels
plt.title('Community Clusters (Color-coded by Community)')
plt.xlabel('Subreddit')
plt.ylabel('Community')

plt.tight_layout()
plt.show()
