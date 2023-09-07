from source.clean_00 import cleanup_tuple


def test_cleanup_tuple_returns_formatted_string_with_job_title_and_score_when_given_tuple_with_job_title_and_score():
    tup = ("Job Title", 90.0)
    result = cleanup_tuple(tup)

    assert result == "Job Title, 90.0%"
