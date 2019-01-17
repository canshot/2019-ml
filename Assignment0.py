import matplotlib.pyplot as plt
import numpy as np
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
import os, glob

# Entire gutenberg dataset
corpus=[]
for filename in sorted(glob.glob(os.path.join('gutenberg/', '*.rtf'))):
    file=open(filename,"r",encoding="utf8")
    text=file.read()
    corpus.append(text)
    file.close()
print("Read", len(corpus), "books from gutenberg dataset.\n-------------------------------")

words = []
for text in corpus:
    for w in word_tokenize(text):
        words.append(w)

print("Number of words in the list: ", len(words))

""" 
A counter is just like a dictionary in python. It is a very import tool to know about for NLP purposes. It keeps a track
of the count of each element.
Elements in the counter are based on key and value. Key represents the words and values would be the count of the word.
""" 
from collections import Counter
counts = Counter(words)

# Print the 50 most frequently occurring words in the corpus
print("Top 50 Frequent words in corpus:\n------------------------------\n", counts.most_common(50))

"""
This is a way of iterating through the items of the Counter. I am just getting the top 50 words in terms of frequencies
key represents the words and values represents the value for the key you are iterating.
"""
word = []
word_count = []
for key,value in counts.most_common(50):
    print(key, ":", value)
    word.append(key)
    word_count.append(value)

# Plotting the top 50 words with word displayed on the x axis
y_pos = np.arange(50)
plt.figure(figsize=(12,10))
plt.bar(y_pos, word_count, align='center', alpha=0.5)
plt.xticks(y_pos, word,rotation='vertical')
plt.ylabel('Frequency')
plt.xlabel('Words')
plt.title('50 Most Frequent Words')
plt.show()
