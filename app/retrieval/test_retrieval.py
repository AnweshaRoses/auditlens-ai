from app.ingestion.pdf_loader import extract_pages_from_pdf
from app.ingestion.chunker import chunk_pages
from app.embeddings.embedder import Embedder
from app.retrieval.vector_store import VectorStore


PDF_PATH = "data/raw/adityatb.pdf"


# 1. Extract pages
pages = extract_pages_from_pdf(PDF_PATH)

print(f"Pages extracted: {len(pages)}")


# 2. Create chunks
chunks = chunk_pages(pages)

print(f"Chunks created: {len(chunks)}")


# 3. Create embeddings
embedder = Embedder()

texts = [
    chunk["text"]
    for chunk in chunks
]

embeddings = embedder.encode(texts)

print(f"Embedding shape: {embeddings.shape}")


# 4. Create vector store
vector_store = VectorStore()

vector_store.add(
    embeddings,
    chunks,
)


# 5. Ask a question
question = "What are the company's current assets?"

query_embedding = embedder.encode(
    [question]
)


# 6. Search
results = vector_store.search(
    query_embedding,
    top_k=5,
)


# 7. Display results
print("\nTop results:\n")

for result in results:

    print(
        f"Score: {result['score']:.4f} | "
        f"Page: {result['page']} | "
        f"Source: {result['source_type']}"
    )

    print(result["text"][:500])

    print("-" * 80)