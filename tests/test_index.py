from docfinder.index import build_chunk_index

def test_build_chunk_index_creates_records():
    documents = [
        {
            "source": "notes.txt",
            "text": "a" * 1200,
        }
    ]

    #TODO

def test_build_chunk_index_handles_multiple_documents():
    documents = [
        {"source": "first.txt", "text": "This is the first document's text."},
        {"source": "second.txt", "text": "The second document's text is this sentence."},
    ]
    #TODO