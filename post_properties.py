import pandas as pd
import networkx as nx
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/soc-redditHyperlinks-body.tsv", sep="\t") #convert csv to df
G = nx.DiGraph() # create graph
# add nodes and edges from df
for _, row in df.iterrows():
    source = row[0]
    destination = row[1]
    G.add_edge(source, destination)
    break

# Make the first 18 properties from the sixth column into multiple columns of floats properties
properties = df.iloc[:, 5].apply(lambda x: list(map(float, x.split(',')))[:18])
property_columns = [f'prop_{i+1}' for i in range(18)]
df_properties = pd.DataFrame(properties.tolist(), columns=property_columns)
df = pd.concat([df.iloc[:, [0, 1]], df_properties], axis=1)

# Create target variable (1 if there's an edge, 0 if there's no edge)
df['edge_exists'] = df.apply(lambda row: 1 if G.has_edge(row[0], row[1]) else 0, axis=1)

# Define the feature set (18 properties)
X = df[property_columns]
y = df['edge_exists']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize, train, and predict the logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Get coefficients of logistic regression model
importance = model.coef_[0]

# Bar plot of Property importance
plt.figure(figsize=(10, 6))
plt.barh(property_columns, importance)
plt.xlabel('Coefficient Value')
plt.title('Property Importance')
plt.savefig('post_properties_results/post_properties_coeff.png')

# Plot the distribution of each property
fig, axes = plt.subplots(6, 3, figsize=(15, 20))  # Create subplots for 18 properties
axes = axes.flatten()

for i, prop in enumerate(property_columns):
    axes[i].hist(df[prop], bins=30, edgecolor='black', alpha=0.7)
    axes[i].set_title(f'Distribution of {prop}')
    axes[i].set_xlabel('Value')
    axes[i].set_ylabel('Frequency')

plt.tight_layout()
plt.title('Property Importance')
plt.savefig(f'post_properties_results/{prop}_dist.png')