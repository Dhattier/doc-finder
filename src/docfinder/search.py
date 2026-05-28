from typing import Any

import numpy as np

from docfinder.embeddings import Embedder, embed_texts


def rank_chunks(
    query: str,
    records: list[dict[str, Any]],
    vectors: np.ndarray,
    embedder: Embedder,
    top_k: int = 5,
) -> list[dict[str, Any]]:
    """Rank chunk records by semantic similarity to a query."""
    if not query.strip():
        raise ValueError("query cannot be blank")

    if top_k <= 0:
        raise ValueError("top_k must be positive")

    if len(records) != len(vectors):
        raise ValueError("records and vectors must have the same length")

    if not records:
        return []

    query_vector = embed_texts([query], embedder)[0]
    scores = vectors @ query_vector

    ranked_indices = np.argsort(scores)[::-1][:top_k]

    results = []

    for index in ranked_indices:
        record = records[int(index)].copy()
        record["score"] = float(scores[index])
        results.append(record)

    return results