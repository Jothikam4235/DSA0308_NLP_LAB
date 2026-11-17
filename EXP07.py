import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
text = "The students are studying natural language processing."
words = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(words)
print("Jothika M 192324235")
print("Word\t\tPOS Tag")
print("--------------------------")
for word, tag in pos_tags:
    print(f"{word:<18}{tag}")