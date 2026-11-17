import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('punkt_tab')
nltk.download('omw-1.4')
sentence = "I went to the bank to deposit money"
words = word_tokenize(sentence)
sense = lesk(words, 'bank')
print("Jothika M 192324235")
print("Sentence:", sentence)
print("\nWord: bank")
if sense:
    print("Meaning:", sense.definition())
    print("Synset:", sense.name())
else:
    print("No meaning found")