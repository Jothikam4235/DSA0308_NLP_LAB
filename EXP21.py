import nltk
from nltk import RegexpParser

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')
nltk.download('omw-1.4')

text = "The intelligent student reads a book"

words = nltk.word_tokenize(text)

pos_tags = nltk.pos_tag(words)

grammar = """
NP: {<DT>?<JJ>*<NN.*>+}
"""

parser = RegexpParser(grammar)

tree = parser.parse(pos_tags)

print("Jothika M 192324235")
print("Input Sentence:", text)
print("\nNoun Phrases and Meanings:")
print("--------------------------------")

from nltk.corpus import wordnet

for subtree in tree.subtrees():
    if subtree.label() == 'NP':
        phrase = " ".join(word for word, tag in subtree.leaves())
        print("Noun Phrase:", phrase)

        for word, tag in subtree.leaves():
            if tag.startswith('NN'):
                synsets = wordnet.synsets(word)
                if synsets:
                    print(word, "->", synsets[0].definition())
        print()