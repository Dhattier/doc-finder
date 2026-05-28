from docfinder.reporting import format_search_results


def test_format_search_results_includes_query_and_result():
    results = [
        {
            "source": "cloud_security.txt",
            "score": 0.91234,
            "text": "Credential theft is a major cloud risk.",
        }
    ]

    output = format_search_results("cloud risks", results)

    assert "Query: cloud risks" in output
    assert "cloud_security.txt" in output
    assert "Score: 0.912" in output
    assert "Credential theft" in output


def test_format_search_results_handles_empty_results():
    output = format_search_results("missing topic", [])

    assert "No results found." in output