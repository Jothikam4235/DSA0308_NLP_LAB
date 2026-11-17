import nltk
from nltk.tokenize import word_tokenize
from nltk import RegexpTagger
text = "The students are studying quickly and intelligent systems"
patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*ly$', 'RB'),
    (r'.*ous$', 'JJ'),
    (r'.*s$', 'NNS'),
    (r'^The$', 'DT'),
    (r'^and$', 'CC'),
    (r'^are$', 'VBP'),
    (r'.*', 'NN')
]
tagger = RegexpTagger(patterns)
words = word_tokenize(text)
tagged_words = tagger.tag(words)
print("Jothika M 192324235")
print("Word\t\tPOS Tag")
print("--------------------------")
for word, tag in tagged_words:
    print(f"{word:<18}{tag}")