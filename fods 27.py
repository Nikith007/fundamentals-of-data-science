# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample dataset (for demonstration purposes)
data = {
    'age': [25, 45, 35, 50, 23, 30, 33, 42],
    'monthly_usage': [200, 150, 300, 80, 400, 150, 120, 100],
    'contract_length': [12, 24, 24, 12, 12, 24, 24, 12],
    'churn': [0, 1, 0, 1, 0, 1, 0, 1]
}

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Define features (X) and target (y)
X = df[['age', 'monthly_usage', 'contract_length']]  # Features
y = df['churn']  # Target: churn (0 for not churned, 1 for churned)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Test the model's accuracy on the test set
y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# Take user input for a new customer's features
age = int(input("Enter the customer's age: "))
monthly_usage = float(input("Enter the customer's monthly usage (in minutes): "))
contract_length = int(input("Enter the contract length (in months): "))

# Predict churn for the new customer
new_customer = np.array([[age, monthly_usage, contract_length]])
predicted_churn = model.predict(new_customer)

# Output the result
if predicted_churn[0] == 1:
    print("The customer is likely to churn.")
else:
    print("The customer is not likely to churn.")
