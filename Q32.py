import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = pd.read_csv("D:/Slot-D/fods/code/Q32sample.csv")
data['Location'] = data['Location'].map({'Suburb': 0, 'City Center': 1})
X = data[['Size (sq ft)', 'Bedrooms', 'Location']]
y = data['Price ($)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
for i, price in enumerate(predictions):
    print(f'Predicted price for house {i + 1}: ${price:.2f}')
