import nltk
from nltk import CFG
from nltk.parse import ChartParser
grammar = CFG.fromstring("""
S -> NP_SG VP_SG | NP_PL VP_PL
NP_SG -> Det_SG N_SG
NP_PL -> Det_PL N_PL
VP_SG -> V_SG
VP_PL -> V_PL
Det_SG -> 'the'
Det_PL -> 'the'
N_SG -> 'student' | 'boy'
N_PL -> 'students' | 'boys'
V_SG -> 'plays' | 'reads'
V_PL -> 'play' | 'read'
""")
parser = ChartParser(grammar)
sentences = [
    "the student plays",
    "the students play",
    "the student play",
    "the students plays"
]
print("Jothika M 192324235")
for sentence in sentences:
    words = sentence.split()
    trees = list(parser.parse(words))
    if trees:
        print(sentence, "-> Grammatically Correct")
    else:
        print(sentence, "-> Agreement Error")