import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
nltk.download('stopwords')

text = "Natural language processing is a branch of artificial intelligence. It helps computers understand human language. Machine learning is used in NLP applications."

sentences = sent_tokenize(text)

stop_words = set(stopwords.words('english'))

print("Jothika M 192324235")
print("Input Text:")
print(text)

print("\nCoherence Evaluation:")
print("--------------------------------")

total_words = 0

for i, sentence in enumerate(sentences):
    words = word_tokenize(sentence.lower())
    meaningful_words = [w for w in words if w.isalpha() and w not in stop_words]
    total_words += len(meaningful_words)

    print("Sentence", i + 1, ":", sentence)
    print("Meaningful Words:", meaningful_words)

score = total_words / len(sentences)

print("\nCoherence Score:", round(score, 2))

if score >= 4:
    print("Text is Coherent")
else:
    print("Text has Low Coherence")