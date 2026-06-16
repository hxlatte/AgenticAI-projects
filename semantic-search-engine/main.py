import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = [
    "Transformers power modern language models.",
    "React is a frontend JavaScript library.",
    "Pandas is used for data analysis.",
    "Python is a popular programming language.",
    "Machine learning helps computers learn from data."
]

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert documents to embeddings
document_embeddings = model.encode(documents)

# Take user query
query = input("Enter your search query: ")

# Convert query to embedding
query_embedding = model.encode([query])

# Calculate similarity scores
similarities = cosine_similarity(
    query_embedding,
    document_embeddings
)

# Find best match
best = np.argmax(similarities)

print("\nMost Relevant Document:")
print(documents[best])