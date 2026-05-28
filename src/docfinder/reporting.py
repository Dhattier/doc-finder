from typing import Any


def format_search_results(query: str, results: list[dict[str, Any]]) -> str:
    """Format ranked search results for terminal output."""
    lines = [f"Query: {query}", "", "Top Results", "-" * 40]

    if not results:
        lines.append("No results found.")
        return "\n".join(lines)

    for rank, result in enumerate(results, start=1):
        source = result.get("source", "unknown")
        score = result.get("score", 0.0)
        text = result.get("text", "").strip()

        lines.extend(
            [
                "",
                f"{rank}. {source}",
                f"Score: {score:.3f}",
                "",
                text,
                "-" * 40,
            ]
        )

    return "\n".join(lines)