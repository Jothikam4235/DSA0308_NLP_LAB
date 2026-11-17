import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["playing", "played", "plays", "running", "runner",
         "studies", "studying", "connected", "connection", "happiness"]
print("Jothika M 192324235")
print("Original Word\tStemmed Word")
print("--------------------------------")
for word in words:
    stem = stemmer.stem(word)
    print(f"{word:<18}{stem}")