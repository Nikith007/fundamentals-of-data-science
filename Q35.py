import pandas as pd
from sklearn.cluster import KMeans
data = pd.read_csv("D:/Slot-D/fods/code/Q35sample.csv")
X = data[['Total Spent ($)', 'Frequency of Visits']]
kmeans = KMeans(n_clusters=3, random_state=42)
data['Segment'] = kmeans.fit_predict(X)
print(data[['Customer ID', 'Segment']])
