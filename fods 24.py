import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Step 1: Create a synthetic dataset of patients with symptoms and condition labels (0 = no condition, 1 = has condition)
data = {
    'Symptom1': np.random.rand(100),
    'Symptom2': np.random.rand(100),
    'Symptom3': np.random.rand(100),
    'Condition': np.random.randint(0, 2, 100)
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Step 2: Split the dataset into features (X) and target (y)
X = df.drop('Condition', axis=1)  # Features (Symptom1, Symptom2, Symptom3)
y = df['Condition']  # Target (Condition)

# Step 3: Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 5: Take user input for new patient symptoms and value of k
new_symptom1 = float(input("Enter symptom 1 value: "))
new_symptom2 = float(input("Enter symptom 2 value: "))
new_symptom3 = float(input("Enter symptom 3 value: "))
k = int(input("Enter the value of k (number of neighbors): "))

# Prepare the new patient's symptoms in the correct format for prediction
new_patient = np.array([[new_symptom1, new_symptom2, new_symptom3]])
new_patient = scaler.transform(new_patient)  # Standardize the new patient's symptoms

# Step 6: Create and train the KNN classifier
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Step 7: Predict the condition for the new patient
prediction = knn.predict(new_patient)

# Step 8: Output the prediction result
if prediction[0] == 1:
    print("The patient is predicted to have the medical condition.")
else:
    print("The patient is predicted NOT to have the medical condition.")
