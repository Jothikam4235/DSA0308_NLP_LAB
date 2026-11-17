import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('omw-1.4')
word = "computer"
synsets = wordnet.synsets(word)
print("Jothika M 192324235")
print("Word:", word)
print("\nSynsets and Meanings:")
print("--------------------------------")
for syn in synsets:
    print("Synset:", syn.name())
    print("Meaning:", syn.definition())
    print("Examples:", syn.examples())
    print()