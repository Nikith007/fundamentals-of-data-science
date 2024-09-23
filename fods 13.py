import os
from collections import Counter
import string

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words

if not os.path.isfile('sample_text.txt'):
    with open('sample_text.txt', 'w') as f:
        f.write("This is a sample text for word frequency analysis. This text is just for testing.")

with open('sample_text.txt', 'r') as file:
    text = file.read()

words = preprocess_text(text)

word_count = Counter(words)

print("Word Frequency Distribution:")
for word, count in word_count.items():
    print(f"{word}: {count}")
