from docfinder.config import DocFinderConfig, load_config


def test_load_config_uses_defaults_when_file_missing(tmp_path):
    config = load_config(tmp_path / "missing.yaml")

    assert isinstance(config, DocFinderConfig)
    assert config.docs_path.name == "sample_docs"
    assert config.chunk_size == 500


def test_load_congi_reads_yaml_values(tmp_path):
    config_file = tmp_path / "config.yaml"
    config_file.write_text(
        """
docs_path: notes
index_dir: local_index
chunk_size: 300
chunk_overlap: 50
top_k: 3
include_extensions:
    - .txt
    - .md
""",
        encoding="utf-8",
    )

    config = load_config(config_file)

    assert config.docs_path.name == "notes"
    assert config.index_dir.name == "local_index"
    assert config.chunk_size == 300
    assert config.chunk_overlap == 50
    assert config.top_k == 3
    assert ".md" in config.include_extensions