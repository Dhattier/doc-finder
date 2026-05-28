from pathlib import Path

import typer
from rich.console import Console

from docfinder.config import load_config
from docfinder.ingest import load_documents
from docfinder.index import build_chunk_index

app = typer.Typer(help="Local semantic search for small text document collections.")
console = Console()


@app.command()
def ingest(
    docs_path: Path | None = typer.Argument(None, help="Folder containing .txt documents."),
    config_path: Path = typer.Option("config.yaml", "--config", "-c"),
) -> None:
    """Load documents and build chunk records."""
    config = load_config(config_path)
    target_docs_path = docs_path or config.docs_path

    documents = load_documents(target_docs_path)
    records = build_chunk_index(
        documents,
        chunk_size=config.chunk_size,
        chunk_overlap=config.chunk_overlap,
    )

    console.print(f"Loaded {len(documents)} documents.")
    console.print(f"Created {len(records)} chunks.")

    # TODO: Persist records to index.jsonl and embeddings to vectors.npy.


@app.command()
def search(
    query: str = typer.Argument(..., help="Search query."),
    config_path: Path = typer.Option("config.yaml", "--config", "-c"),
) -> None:
    """Search the local index."""
    config = load_config(config_path)

    console.print(f"Search is not fully implemented yet.")
    console.print(f"Query: {query}")
    console.print(f"Index directory: {config.index_dir}")

    # TODO: Load records/vectors, embed the query, rank chunks, and format results.


if __name__ == "__main__":
    app()