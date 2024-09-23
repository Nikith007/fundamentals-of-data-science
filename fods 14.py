import pandas as pd

# Sample data representing the sales data (including customer age)
data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Age': [25, 30, 22, 40, 25, 30, 22, 40],
    'PurchaseAmount': [100, 150, 200, 250, 100, 150, 200, 250]
}

# Load the data into a pandas DataFrame
df = pd.DataFrame(data)

# Calculate the frequency distribution of the 'Age' column
age_distribution = df['Age'].value_counts()

# Display the frequency distribution
print("Frequency Distribution of Customer Ages:")
print(age_distribution)
