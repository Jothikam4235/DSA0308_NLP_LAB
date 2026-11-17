import nltk
from nltk.corpus import brown
from nltk.tag import UnigramTagger
nltk.download('brown')
nltk.download('universal_tagset')
tagged_sentences = brown.tagged_sents(tagset='universal')
train_data = tagged_sentences[:4000]
test_data = tagged_sentences[4000:4500]
tagger = UnigramTagger(train_data)
text = "The students are studying natural language processing"
words = nltk.word_tokenize(text)
pos_tags = tagger.tag(words)
print("Jothika M 192324235")
print("Word\t\tPOS Tag")
print("--------------------------")
for word, tag in pos_tags:
    print(f"{word:<18}{tag}")