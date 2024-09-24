# Import required libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Generate a sample housing dataset (for demonstration purposes)
data = {
    'area': [1500, 1700, 1800, 2400, 3000, 3500],
    'bedrooms': [3, 3, 4, 4, 5, 6],
    'location_score': [7, 8, 6, 9, 10, 10],
    'price': [300000, 350000, 370000, 450000, 600000, 700000]
}

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Define features (X) and target (y)
X = df[['area', 'bedrooms', 'location_score']]  # Features: area, bedrooms, location_score
y = df['price']  # Target: price

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Take user input for a new house's features
area = float(input("Enter the area of the house (in sqft): "))
bedrooms = int(input("Enter the number of bedrooms: "))
location_score = float(input("Enter the location score (1-10): "))

# Predict the price of the new house based on input features
new_house = np.array([[area, bedrooms, location_score]])
predicted_price = model.predict(new_house)

# Output the predicted price
print(f"The predicted price of the house is: ${predicted_price[0]:,.2f}")
