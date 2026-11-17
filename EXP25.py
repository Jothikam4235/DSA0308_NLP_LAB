from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

prompt = "Explain Natural Language Processing in simple words."

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print("Jothika M 192324235")
print("Input Prompt:", prompt)
print("\nGenerated Text:")
print(response.output_text)