import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
text = "The students are studying intelligent system in universities"
words = text.split()
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
print("Jothika M 192324235")
print(f"{'Word':<18}{'Stem':<18}{'Lemma':<18}")
print("-" * 54)
for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print(f"{word:<18}{stem:<18}{lemma:<18}")