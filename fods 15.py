import pandas as pd

data = {
    'PostID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Likes': [10, 20, 10, 50, 20, 10, 50, 100]
}

df = pd.DataFrame(data)

likes_distribution = df['Likes'].value_counts()
print("Frequency Distribution of Likes Among Posts:")
print(likes_distribution)
