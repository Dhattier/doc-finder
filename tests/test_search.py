import numpy as np
import pytest

from docfinder.search import rank_chunks


class FakeEmbedder:
    def encode(self, texts: list[str]) -> np.ndarray:
        vectors = []

        for text in texts:
            if "cloud" in text.lower():
                vectors.append([1.0, 0.0, 0.0])
            elif "network" in text.lower():
                vectors.append([0.0, 1.0, 0.0])
            else:
                vectors.append([0.0, 0.0, 1.0])

        return np.array(vectors, dtype=np.float32)


def test_rank_chunks_returns_most_similar_chunk_first():
    records = [
        {"chunk_id": 0, "source": "cloud.txt", "text": "cloud security risks"},
        {"chunk_id": 1, "source": "network.txt", "text": "network routing notes"},
    ]

    vectors = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
        ],
        dtype=np.float32,
    )

    results = rank_chunks(
        query="cloud access controls",
        records=records,
        vectors=vectors,
        embedder=FakeEmbedder(),
        top_k=1,
    )

    assert len(results) == 1
    assert results[0]["source"] == "cloud.txt"
    assert results[0]["score"] > 0.9


def test_rank_chunks_rejects_blank_query():
    with pytest.raises(ValueError):
        rank_chunks(
            query="   ",
            records=[],
            vectors=np.empty((0, 3), dtype=np.float32),
            embedder=FakeEmbedder(),
        )


def test_rank_chunks_rejects_mismatched_records_and_vectors():
    records = [{"chunk_id": 0, "source": "cloud.txt", "text": "cloud security"}]
    vectors = np.empty((0, 3), dtype=np.float32)

    with pytest.raises(ValueError):
        rank_chunks(
            query="cloud",
            records=records,
            vectors=vectors,
            embedder=FakeEmbedder(),
        )