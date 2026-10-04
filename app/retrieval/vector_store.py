import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension: int = 384):
        self.dimension = dimension

        self.index = faiss.IndexFlatIP(dimension)

        self.chunks = []

    def add(
        self,
        embeddings: np.ndarray,
        chunks: list[dict],
    ):
        embeddings = embeddings.astype("float32")

        self.index.add(embeddings)

        self.chunks.extend(chunks)

    def search(
        self,
        query_embedding: np.ndarray,
        top_k: int = 5,
    ):
        query_embedding = query_embedding.astype("float32")

        scores, indices = self.index.search(
            query_embedding,
            top_k,
        )

        results = []

        for score, index in zip(
            scores[0],
            indices[0],
        ):
            if index == -1:
                continue

            result = self.chunks[index].copy()

            result["score"] = float(score)

            results.append(result)

        return results