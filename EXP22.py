import nltk

nltk.download('punkt_tab')

text = "John is a student. He studies computer science. John likes programming. He works hard."

sentences = nltk.sent_tokenize(text)

previous_name = None

print("Jothika M 192324235")
print("Original Text:")
print(text)

print("\nReference Resolution:")
print("--------------------------------")

for sentence in sentences:
    words = nltk.word_tokenize(sentence)

    if "John" in words:
        previous_name = "John"

    if "He" in words and previous_name:
        sentence = sentence.replace("He", previous_name)

    print(sentence)