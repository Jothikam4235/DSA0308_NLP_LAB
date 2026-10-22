import re
text = "I want to travel from chennai to madurai with flight number 24235"
if re.search(r"mumbai", text, re.IGNORECASE):
    text = re.sub(r"mumbai", "bangalore", text, flags=re.IGNORECASE)
if re.search(r"chennai", text, re.IGNORECASE):
    text = re.sub(r"chennai", "USA", text, flags=re.IGNORECASE)
if re.search(r"\b\d{5}\b", text):
    text = re.sub(r"\b\d{5}\b", "192324235", text)
print("Updated Text:", text)