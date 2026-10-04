import json

from app.ingestion.pdf_loader import extract_pages_from_pdf
from app.ingestion.chunker import chunk_pages
from app.embeddings.embedder import Embedder
from app.retrieval.vector_store import VectorStore


PDF_PATH = "data/raw/adityatb.pdf"
QUESTIONS_PATH = "data/evaluation/questions.json"


def load_questions():
    with open(QUESTIONS_PATH, "r") as file:
        return json.load(file)


def build_retriever():

    pages = extract_pages_from_pdf(PDF_PATH)

    chunks = chunk_pages(pages)

    print(f"Pages extracted: {len(pages)}")
    print(f"Chunks created: {len(chunks)}")

    embedder = Embedder()

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = embedder.encode(texts)

    print(f"Embedding shape: {embeddings.shape}")

    vector_store = VectorStore()

    vector_store.add(
        embeddings,
        chunks,
    )

    return embedder, vector_store


def evaluate_recall(
    embedder,
    vector_store,
    questions,
    top_k,
):

    hits = 0

    for item in questions:

        question = item["question"]
        expected_pages = set(item["expected_pages"])

        query_embedding = embedder.encode(
            [question]
        )

        results = vector_store.search(
            query_embedding,
            top_k=top_k,
        )

        retrieved_pages = {
            result["page"]
            for result in results
        }

        found = bool(
            expected_pages.intersection(
                retrieved_pages
            )
        )

        if found:
            hits += 1

        print(
            f"\nQuestion: {question}"
        )

        print(
            f"Expected pages: "
            f"{sorted(expected_pages)}"
        )

        print(
            f"Retrieved pages: "
            f"{sorted(retrieved_pages)}"
        )

        print(
            f"Result: {'HIT' if found else 'MISS'}"
        )

    recall = hits / len(questions)

    return recall


if __name__ == "__main__":

    questions = load_questions()

    embedder, vector_store = build_retriever()

    print("\n" + "=" * 60)
    print("AUDITLENS RETRIEVAL EVALUATION")
    print("=" * 60)

    for k in [1, 3, 5]:

        print(
            f"\n{'-' * 60}"
        )

        print(
            f"Evaluating Recall@{k}"
        )

        recall = evaluate_recall(
            embedder,
            vector_store,
            questions,
            top_k=k,
        )

        print(
            f"\nRecall@{k}: {recall:.2%}"
        )