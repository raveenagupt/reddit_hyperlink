import pandas as pd
import matplotlib.pyplot as plt

def convert(name):
    return top_10_subreddits.index(name)


'''
df1 = pd.read_csv('soc-redditHyperlinks-body.tsv', sep='\t')  # Replace with your actual file path


# Ensure the 'source' and 'target' columns exist (you can replace 'source' and 'target' with your actual column names)
# Count the degree for each subreddit, considering both source and target
degree_counts1 = pd.concat([df1['SOURCE_SUBREDDIT'], df1['TARGET_SUBREDDIT']]).value_counts()

# Determine the middle 10 rows
total_rows = len(degree_counts1)
print(total_rows)
start_index = 1000  # Middle 10, so 5 rows before the middle
end_index = 1010   # Middle 10, so 5 rows after the middle

# Get the middle 10 rows using iloc
middle_10 = degree_counts1.iloc[start_index:end_index]

print(middle_10)
'''

top_10_subreddits = ['gamedevclassifieds', 'askcarsales', 'kossacks_for_sanders', 'nflstreams', 'santaslittlehelpers', 'loleventvods',
                     'iwantout', 'crusaderkings', 'denvernuggets', 'askseddit']
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
'''
# Plot the degree of each top subreddit over time
plt.figure(figsize=(10, 6))
colors = {0: 'red', 1: 'blue', 2: 'green', 3: 'red', 4: 'blue',5: 'blue',6: 'blue',7: 'blue',8: 'blue',9: 'blue'}
for subreddit in top_10_subreddits:
    print(colors[convert(subreddit)])
    plt.scatter(degree_df['timestamp'], degree_df['degree'], label =subreddit, color = colors[convert(subreddit)])

'''
plt.figure(figsize=(10, 6))
# Plot each subreddit on the same graph

for subreddit in top_10_subreddits[0:5]:
    if subreddit in degree_df_pivot.index:
        degree_df_pivot.loc[subreddit].plot(label=subreddit, kind='line')

# Customize the plot
plt.title('Degree of Upper 5 Subreddits Over Time (3 1/3-Year Period)')
plt.xlabel('Timestamp')
plt.ylabel('Degree')
plt.legend(title="Subreddits", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to prevent overlap of labels

# Show the plot
plt.show()
plt.figure(figsize=(10, 6))
# Plot each subreddit on the same graph
for subreddit in top_10_subreddits[5:10]:
    if subreddit in degree_df_pivot.index:
        degree_df_pivot.loc[subreddit].plot(label=subreddit, kind='line')

# Customize the plot
plt.title('Degree of Upper 5 Subreddits Over Time (3 1/3-Year Period)')
plt.xlabel('Timestamp')
plt.ylabel('Degree')
plt.legend(title="Subreddits", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to prevent overlap of labels

# Show the plot
plt.show()

