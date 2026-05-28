from docfinder.chunking import chunk_text


def build_chunk_index(
        documents: list[dict[str,str]],
        chunk_size: int = 500,
        chunk_overlap: int = 75,
) -> list[dict[str,str | int]]:
    """Converts loaded documents into searchable chunk records"""
    records = []
    chunk_id = 0

    for document in documents:
        source = document["source"]
        text = document["text"]

        chunks = chunk_text(
            text,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        for position, chunk in enumerate(chunks):
            records.append(
                {
                    "chunk_id": chunk_id,
                    "source": source,
                    "chunk_index": position,
                    "text": chunk,
                }
            )
            chunk_id = 1

    return records