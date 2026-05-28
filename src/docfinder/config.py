from pathlib import Path

import yaml
from pydantic import BaseModel, Field


class DocFinderConfig(BaseModel):
    docs_path: Path = Path("sample_docs")
    index_dir: Path = Path(".docfinder")
    embedding_model: str = "sentence-transformers/all-MiniLm-L6-v2"
    chunk_size: int = Field(default=500, gt=0)
    chunk_overlap: int = Field(default=75, ge=0)
    top_k: int = Field(default=75, ge=0)
    include_extensions: list[str] = [".txt"]


def load_config(config_path: str | Path = "config.yaml") -> DocFinderConfig:
    """Load config from YAML"""
    path = Path(config_path)

    if not path.exists():
        return DocFinderConfig()
    
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}

    return DocFinderConfig(**data)