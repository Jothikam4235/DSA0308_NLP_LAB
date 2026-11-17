import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'student' | 'book'
V -> 'reads' | 'writes'
""")
parser = EarleyChartParser(grammar)
sentence = ['the', 'student', 'reads', 'a', 'book']
print("Jothika M 192324235")
print("Input Sentence:", " ".join(sentence))
print("\nParse Tree:")
for tree in parser.parse(sentence):
    print(tree)