import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'boy' | 'girl' | 'book'
V -> 'reads' | 'likes'
""")
parser = RecursiveDescentParser(grammar)
sentence = ['the', 'boy', 'reads', 'a', 'book']
print("Jothika M 192324235")
print("Input Sentence:", " ".join(sentence))
print("\nParse Tree:")
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()