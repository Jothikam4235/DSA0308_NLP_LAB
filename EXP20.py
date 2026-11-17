from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Natural language processing is a branch of artificial intelligence",
    "Machine learning is used in artificial intelligence",
    "Python is a programming language",
    "Natural language processing helps computers understand human language"
]

query = "natural language processing"

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

query_vector = vectorizer.transform([query])

similarity = cosine_similarity(query_vector, tfidf_matrix)

print("Jothika M 192324235")
print("Search Query:", query)
print("\nDocument Ranking:")
print("--------------------------------")

ranking = similarity[0].argsort()[::-1]

for i in ranking:
    print("Document", i + 1, "-> Score:", round(similarity[0][i], 4))
    print(documents[i])
    print()