import re

def recognize_dialog_act(sentence):
    sentence = sentence.lower()

    if re.search(r'\b(hello|hi|hey)\b', sentence):
        return "Greeting"

    elif re.search(r'\b(thank you|thanks)\b', sentence):
        return "Thanking"

    elif re.search(r'\b(bye|goodbye|see you)\b', sentence):
        return "Goodbye"

    elif sentence.endswith('?'):
        return "Question"

    elif re.search(r'\b(please|could you|can you)\b', sentence):
        return "Request"

    else:
        return "Statement"


dialog = [
    "Hello, how are you?",
    "Can you help me?",
    "What is NLP?",
    "Thank you",
    "I am learning Python",
    "Goodbye"
]

print("Jothika M 192324235")
print("Dialog Act Recognition")
print("------------------------------")

for sentence in dialog:
    act = recognize_dialog_act(sentence)
    print(sentence, "->", act)