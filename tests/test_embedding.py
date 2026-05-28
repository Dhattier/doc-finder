import numpy as np
import pytest

from docfinder.embeddings import embed_texts, normalize_vectors


class FakeEmbedder:
    def encode(self, texts: list[str]) -> np.ndarray:
        vectors = []

        for text in texts:
            if "cloud" in text:
                vectors.append([1.0, 0.0, 0.0])
            else:
                vectors.append([0.0, 1.0, 0.0])

        return np.array(vectors, dtype=np.float32)


def test_normalize_vectors_returns_unit_vectors():
    vectors = np.array([[3.0, 4.0]], dtype=np.float32)

    normalized = normalize_vectors(vectors)

    assert np.allclose(np.linalg.norm(normalized, axis=1), [1.0])


def test_normalize_vectors_rejects_1d_arrays():
    with pytest.raises(ValueError):
        normalize_vectors(np.array([1.0, 2.0, 3.0]))


def test_embed_texts_uses_embedder_and_normalizes_vectors():
    texts = ["cloud security risks", "network routing notes"]

    vectors = embed_texts(texts, FakeEmbedder())

    assert vectors.shape == (2, 3)
    assert np.allclose(np.linalg.norm(vectors, axis=1), [1.0, 1.0])