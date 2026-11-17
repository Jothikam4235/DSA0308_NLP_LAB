import nltk
from nltk.tag import DefaultTagger, UnigramTagger, BrillTaggerTrainer
from nltk.tag.brill import Pos, Word
nltk.download('treebank')
training_data = nltk.corpus.treebank.tagged_sents()
train_data = training_data[:3000]
default_tagger = DefaultTagger('NN')
templates = [
    Pos([-1]),
    Pos([1]),
    Word([-1]),
    Word([1])
]
trainer = BrillTaggerTrainer(default_tagger, templates)
tagger = trainer.train(train_data, max_rules=10)
text = "The students are studying natural language processing"
words = nltk.word_tokenize(text)
tagged_words = tagger.tag(words)
print("Jothika M 192324235")
print("Word\t\tPOS Tag")
print("--------------------------")
for word, tag in tagged_words:
    print(f"{word:<18}{tag}")