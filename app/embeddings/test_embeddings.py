from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

sentences = [
    "Revenue should be recognized when control transfers to the customer.",
    "Revenue recognition occurs when the customer obtains control.",
    "The weather is sunny today."
]

embeddings = model.encode(sentences)

print("Embedding shape:")
print(embeddings.shape)