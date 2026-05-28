from pathlib import Path

SUPPORTED_EXTENSIONS = {".txt"}

def load_documents(docs_path: str | Path) -> list[dict[str, str]]:
    """ Load documents from a directory"""
    path = Path(docs_path)

    if not path.exists():
        raise FileNotFoundError(f"Directory {docs_path} does not exist.")
    
    if not path.is_dir():
        raise NotADirectoryError(f"{docs_path} is not a directory.")

    documents = []

    for file_path in sorted(path.iterdir()):
        if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue
            
        text  = file_path.read_text(encoding="utf-8").strip()

        if not text:
            continue

        documents.append(
            {
            "source": file_path.name,
            "path": str(file_path),
            "text": text,
            }
        )

    return documents