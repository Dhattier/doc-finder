import pytest

from docfinder.ingest import load_documents


def test_load_documents_reads_txt_files(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()

    notes = docs_dir / "notes.txt"
    notes.write_text("This is a test document.", encoding="utf-8")

    documents = load_documents(docs_dir)

    assert len(documents) == 1
    assert documents[0]["source"] == "notes.txt"
    assert documents[0]["text"] == "This is a test document."


def test_load_documents_ignores_unsupported_files(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()

    (docs_dir / "notes.txt").write_text("Keep this.", encoding="utf-8")
    (docs_dir / "notes.pdf").write_text("Ignore this.", encoding="utf-8")

    documents = load_documents(docs_dir)

    assert len(documents) == 1
    assert documents[0]["source"] == "notes.txt"
    assert documents[0]["text"] == "Keep this." 

def test_load_documents_rejects_missing_path():
    with pytest.raises(FileNotFoundError):
        load_documents("nonexistent_dir")