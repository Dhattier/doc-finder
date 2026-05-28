import pytest

from docfinder.chunking import chunk_text

def test_chunk_text_returns_chunks():
    text = "a" * 1200
    chunks = chunk_text(text, chunk_size=500, chunk_overlap=75)
    assert len(chunks) == 3

def test_chunk_text_returns_empty_list_for_blank_text():
    assert chunk_text("   ") == []

def test_chunk_text_rejects_invalid_overlap():
    with pytest.raises(ValueError):
        chunk_text("hello", chunk_size=100, chunk_overlap=100)
        