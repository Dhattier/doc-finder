def chunk_text(text: str, chunk_size: int = 500, chunk_overlap: int = 75) -> list [str]:
    """ Split text into overlapping chunks.
    Args:
        text (str): The text to be chunked.
        chunk_size (int, optional): The size of each chunk. Defaults to 500.
        chunk_overlap (int, optional): The number of overlapping characters between chunks. Defaults to 75.
    Returns:
        list [str]: A list of text chunks.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive.")
    
    if chunk_overlap < 0:
        raise ValueError("chunk_overlap cannot be negative.")
    
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be less than chunk_size.")
    
    cleaned_text = text.strip()

    if not cleaned_text:
        return []
    
    chunks = []
    start = 0

    while start < len(cleaned_text):
        end = start + chunk_size
        chunk = cleaned_text[start:end].strip()

        if chunk:
            chunks.append(chunk)
        
        start += chunk_size - chunk_overlap

    return chunks