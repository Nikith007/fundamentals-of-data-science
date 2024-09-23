import pandas as pd
import string
from collections import Counter

data = {
    'ReviewID': [1, 2, 3, 4, 5],
    'ReviewText': [
        "This product is great! I really love it.",
        "Good quality, but the price is too high.",
        "Not worth the money, I am disappointed.",
        "Excellent product, works perfectly as described.",
        "Very bad experience, I will not recommend it."
    ]
}

df = pd.DataFrame(data)

reviews = df['ReviewText']

def preprocess_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    return text.split()

all_words = []

for review in reviews:
    all_words.extend(preprocess_text(review))

word_freq = Counter(all_words)

print("Top 10 most common words:")
print(word_freq.most_common(10))
