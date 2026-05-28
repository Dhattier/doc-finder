# DocFinder

DocFinder is a small local semantic search tool for text notes.

It can:
- read `.txt`, `.md`, and `.docx` documents from a folder
- split documents into chunks
- embed chunks locally
- save a local index
- search for relevant passages by meaning

## Planned commands

```bash
docfinder ingest sample_docs/
docfinder search "what are the risks of NFV"