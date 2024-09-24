# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Sample dataset (for demonstration purposes)
data = {
    'annual_income': [15, 16, 17, 18, 19, 22, 28, 35, 42, 50],
    'spending_score': [39, 81, 6, 77, 40, 76, 94, 12, 88, 73]
}

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Define features (X)
X = df[['annual_income', 'spending_score']]

# Normalize the data using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# Visualize the clusters
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=kmeans.labels_, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
plt.title('Customer Segments')
plt.xlabel('Annual Income (scaled)')
plt.ylabel('Spending Score (scaled)')
plt.show()

# Take user input for a new customer's features
annual_income = float(input("Enter the customer's annual income: "))
spending_score = float(input("Enter the customer's spending score: "))

# Normalize the input features
new_customer = np.array([[annual_income, spending_score]])
new_customer_scaled = scaler.transform(new_customer)

# Predict the cluster for the new customer
cluster = kmeans.predict(new_customer_scaled)

# Output the result
print(f"The new customer belongs to segment {cluster[0]}.")
