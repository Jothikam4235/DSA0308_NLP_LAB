import spacy
nlp = spacy.load("en_core_web_sm")
text = "Jothika is studying at Saveetha University in Chennai. She works with Google in India."
doc = nlp(text)
print("Jothika M 192324235")
print("Named Entities:")
print("------------------------------")
for ent in doc.ents:
    print(ent.text, "->", ent.label_)