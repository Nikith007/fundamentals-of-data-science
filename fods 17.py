import pandas as pd
import string
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

df = pd.read_csv('data.csv')

def preprocess_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    return words

all_words = []
for feedback in df['feedback']:
    all_words.extend(preprocess_text(feedback))

word_freq = Counter(all_words)

N = int(input("Enter the number of top frequent words to display: "))

most_common_words = word_freq.most_common(N)
print(f"Top {N} most frequent words:")
for word, freq in most_common_words:
    print(f"{word}: {freq}")

words, frequencies = zip(*most_common_words)
plt.figure(figsize=(10, 6))
plt.bar(words, frequencies, color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequencies')
plt.title(f'Top {N} Most Frequent Words in Customer Feedback')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
