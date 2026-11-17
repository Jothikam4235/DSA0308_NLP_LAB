from transformers import pipeline

translator = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
)

text = "Hello, how are you? I am learning Natural Language Processing."

result = translator(text)

print("Jothika M 192324235")
print("English Text:", text)
print("\nFrench Translation:")
print(result[0]['translation_text'])