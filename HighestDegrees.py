import pandas as pd
import matplotlib.pyplot as plt

def convert(name):
    return top_10_subreddits.index(name)




# Load your TSV file
'''
df1 = pd.read_csv('soc-redditHyperlinks-body.tsv', sep='\t')  # Replace with your actual file path


# Ensure the 'source' and 'target' columns exist (you can replace 'source' and 'target' with your actual column names)
# Count the degree for each subreddit, considering both source and target
degree_counts1 = pd.concat([df1['SOURCE_SUBREDDIT'], df1['TARGET_SUBREDDIT']]).value_counts()

# Get the top 10 subreddits with the highest degrees
top_10_subreddits = degree_counts1.head(10)

# Print the top 10 subreddits with their degrees
print("Top 10 subreddits with the highest degrees:")
print(top_10_subreddits)
'''
top_10_subreddits = ['askreddit', 'subredditdrama', 'iama', 'writingprompts', 'leagueoflegends', 'outoftheloop', 'pics', 'circlebroke',
                     'videos', 'conspiracy']
df = pd.read_csv('soc-redditHyperlinks-body.tsv', sep='\t')  # Replace with your actual file path

# Ensure the 'source', 'target', and 'timestamp' columns exist (replace with your actual column names)
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])  # Convert 'timestamp' to datetime format
print(df['TIMESTAMP'].isna().sum())  # Debug: Check for any NaT values in timestamp

# Filter the data to include only the rows with the top 10 subreddits in either source or target
filtered_df = df[df['SOURCE_SUBREDDIT'].isin(top_10_subreddits) | df['TARGET_SUBREDDIT'].isin(top_10_subreddits)]
print("Rows after filtering:", filtered_df.shape[0])

# Create an empty list to store degree counts over time
degree_over_time = []
hash_map = {}
hash_map[0] = 0
hash_map[1] = 0
hash_map[2] = 0
hash_map[3] = 0
hash_map[4] = 0
hash_map[5] = 0
hash_map[6] = 0
hash_map[7] = 0
hash_map[8] = 0
hash_map[9] = 0

# Iterate through the filtered dataset and track the degree for each subreddit over time
for timestamp, group in filtered_df.groupby('TIMESTAMP'):
    print(timestamp)
    source = group["SOURCE_SUBREDDIT"].tolist()[0]
    target = group["TARGET_SUBREDDIT"].tolist()[0]
    subreddit = ''
    # Count the degrees for each subreddit at this timestamp
    if(source in (top_10_subreddits)):
        hash_map[convert(source)] += 1
        subreddit = source
    elif(target in(top_10_subreddits)):
        hash_map[convert(target)] += 1
        subreddit = target
  
    
    degree_over_time.append((timestamp, subreddit, hash_map[convert(subreddit)]))
  
   

# Convert the list of degrees over time into a DataFrame
degree_df = pd.DataFrame(degree_over_time, columns=['timestamp', 'subreddit', 'degree'])

# Pivot the DataFrame to have subreddits as rows and timestamps as columns
degree_df_pivot = degree_df.pivot_table(index='subreddit', columns='timestamp', values='degree', aggfunc='sum', fill_value=0)

# Plot the degree of each top subreddit over time
plt.figure(figsize=(10, 6))

# Plot each subreddit on the same graph
for subreddit in top_10_subreddits:
    if subreddit in degree_df_pivot.index:
        degree_df_pivot.loc[subreddit].plot(label=subreddit, kind='line')

# Customize the plot
plt.title('Degree of Top 10 Subreddits Over Time (3 1/3-Year Period)')
plt.xlabel('Timestamp')
plt.ylabel('Degree')
plt.legend(title="Subreddits", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to prevent overlap of labels

# Show the plot
plt.show()
