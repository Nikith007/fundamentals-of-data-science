# Import required libraries
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features: sepal length, sepal width, petal length, petal width
y = iris.target  # Target: flower species

# Initialize the Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)  # Train the classifier

# Input: Sepal and Petal dimensions for a new flower
sepal_length = float(input("Enter sepal length (in cm): "))
sepal_width = float(input("Enter sepal width (in cm): "))
petal_length = float(input("Enter petal length (in cm): "))
petal_width = float(input("Enter petal width (in cm): "))

# Predict the species
new_flower = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
predicted_species = clf.predict(new_flower)

# Map the predicted species to their names
species_name = iris.target_names[predicted_species[0]]

# Output the predicted species
print(f"The predicted species is: {species_name}")
