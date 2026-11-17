import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser
grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.6] | 'John' [0.4]
VP -> V NP [0.7] | V [0.3]
Det -> 'the' [1.0]
N -> 'book' [0.5] | 'apple' [0.5]
V -> 'reads' [0.6] | 'eats' [0.4]
""")
parser = ViterbiParser(grammar)
sentence = ['John', 'reads', 'the', 'book']
print("Jothika M 192324235")
print("Input Sentence:", " ".join(sentence))
print("\nProbabilistic Parse Tree:")
for tree in parser.parse(sentence):
    print(tree)
    print("Probability:", tree.prob())