import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats

# Data: Age and body fat percentage (%fat) of 18 randomly selected adults
data = {
    'age': [23, 45, 31, 35, 37, 48, 30, 50, 27, 49, 41, 38, 52, 47, 33, 28, 40, 53],
    '%fat': [16.5, 25.4, 18.7, 20.1, 21.2, 26.8, 19.5, 28.4, 17.6, 27.9, 23.1, 21.8, 29.5, 26.5, 18.9, 17.2, 24.6, 30.0]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate mean, median, and standard deviation
mean_age = df['age'].mean()
median_age = df['age'].median()
std_age = df['age'].std()

mean_fat = df['%fat'].mean()
median_fat = df['%fat'].median()
std_fat = df['%fat'].std()

print("Mean Age:", mean_age)
print("Median Age:", median_age)
print("Standard Deviation of Age:", std_age)
print("\nMean %Fat:", mean_fat)
print("Median %Fat:", median_fat)
print("Standard Deviation of %Fat:", std_fat)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.boxplot(df['age'])
plt.title('Boxplot of Age')

plt.subplot(1, 2, 2)
sns.boxplot(df['%fat'])
plt.title('Boxplot of Body Fat Percentage')

plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 6))
sns.scatterplot(x='age', y='%fat', data=df)
plt.title('Scatter Plot: Age vs %Fat')
plt.xlabel('Age')
plt.ylabel('%Fat')
plt.show()

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
stats.probplot(df['age'], dist="norm", plot=plt)
plt.title('Q-Q Plot for Age')

plt.subplot(1, 2, 2)
stats.probplot(df['%fat'], dist="norm", plot=plt)
plt.title('Q-Q Plot for Body Fat Percentage')

plt.tight_layout()
plt.show()
