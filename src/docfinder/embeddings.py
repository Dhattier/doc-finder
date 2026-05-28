from typing import Protocol

import numpy as np


class Embedder(Protocol):
    """Protocol for objects that can embed text."""

    def encode(self, texts: list[str]) -> np.ndarray:
        """Converts text into embedding vectors."""
        ...

class SentenceTransformerEmbedder:
    """Wrapper around sentence-transformers.
    
    Delayed import so tests can run without loading the model."""

    def __init__(self, model_name: str) -> None:
        from sentence_transformers import SentenceTransformer

        self.model = SentenceTransformer(model_name)

    def encode(self, texts: list[str]) -> np.ndarray:
        vectors = self.model.encode(texts, convert_to_numpy=True)
        return np.asanyarray(vectors, dtype=np.float32)
    

def normalize_vectors(vectors: np.array) -> np.ndarray:
    """Normalize vectors so dot product can be used as cosine similarity"""
    if vectors.ndim != 2:
        raise ValueError("vectors must be a 2D array")
    
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1.0

    return vectors / norms


def embed_texts(texts: list[str], embedder: Embedder) -> np.ndarray:
    """Embed and normalize list of texts"""
    if not texts:
        return np.empty((0,0), dtype=np.float32)
    
    vectors = embedder.encode(texts)
    return normalize_vectors(vectors)