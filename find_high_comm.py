import csv
from collections import Counter

# List of file paths for your 6 CSV files
csv_files = ['community_metrics_csvs/average_path_length.csv', 'community_metrics_csvs/clustering_coefficient.csv', 'community_metrics_csvs/density.csv', 'community_metrics_csvs/average_degree.csv', 'community_metrics_csvs/edge_connectivity.csv', 'community_metrics_csvs/node_connectivity.csv']

# Initialize a Counter to keep track of group ID occurrences
counts = Counter()

# Iterate over each CSV file
for csv_file in csv_files:
    try:
        with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header if there is one
            for row in csv_reader:
                community = row[0]
                counts[community] += 1
                
    except FileNotFoundError:
        print(f"Error: File {csv_file} not found.")
    except Exception as e:
        print(f"Error processing file {csv_file}: {e}")
sorted_counts = counts.most_common()
print("Community counts sorted by frequency:")
for community, count in sorted_counts:
    print(f"Community: {community}, Count: {count}")
