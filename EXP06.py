import random
from collections import defaultdict
text = "natural language processing is a part of artificial intelligence natural language processing helps computers understand language"
words = text.lower().split()
bigram_model = defaultdict(list)
for i in range(len(words) - 1):
    bigram_model[words[i]].append(words[i + 1])
def generate_text(start_word, length):
    current_word = start_word
    result = [current_word]
    for i in range(length - 1):
        next_words = bigram_model.get(current_word)
        if not next_words:
            break
        current_word = random.choice(next_words)
        result.append(current_word)
    return " ".join(result)
print("Jothika M 192324235")
print("Bigram Model Text Generation:")
print(generate_text("natural", 8))