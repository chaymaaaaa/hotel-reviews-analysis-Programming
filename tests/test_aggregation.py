import pandas as pd
import pytest

from src.aggregation import aggregate_by_country


@pytest.fixture
def sample_data():
    """
    Create a controlled dataset for aggregation tests.

    Input:
        None.

    Output:
        pandas DataFrame containing sample hotel reviews.
    """

    return pd.DataFrame({
        "Country": [
            "France",
            "France",
            "France",
            "Italy",
            "Italy"
        ],
        "Hotel_ID": [
            "Hotel A",
            "Hotel A",
            "Hotel B",
            "Hotel C",
            "Hotel D"
        ],
        "Reviewer_Score": [
            8.0,
            10.0,
            9.0,
            7.0,
            9.0
        ]
    })


def test_country_grouping(sample_data):
    """Verify that reviews are grouped by country."""

    result = aggregate_by_country(sample_data)

    assert len(result) == 2
    assert set(result["Country"]) == {"France", "Italy"}


def test_review_count(sample_data):
    """Verify the number of reviews per country."""

    result = aggregate_by_country(sample_data)
    result = result.set_index("Country")

    assert result.loc["France", "Number_of_Reviews"] == 3
    assert result.loc["Italy", "Number_of_Reviews"] == 2


def test_hotel_count(sample_data):
    """Verify the number of distinct hotels."""

    result = aggregate_by_country(sample_data)
    result = result.set_index("Country")

    assert result.loc["France", "Number_of_Hotels"] == 2
    assert result.loc["Italy", "Number_of_Hotels"] == 2


def test_average_score(sample_data):
    """Verify the average reviewer score."""

    result = aggregate_by_country(sample_data)
    result = result.set_index("Country")

    assert result.loc["France", "Average_Reviewer_Score"] == 9.0
    assert result.loc["Italy", "Average_Reviewer_Score"] == 8.0


def test_median_score(sample_data):
    """Verify the median reviewer score."""

    result = aggregate_by_country(sample_data)
    result = result.set_index("Country")

    assert result.loc["France", "Median_Reviewer_Score"] == 9.0
    assert result.loc["Italy", "Median_Reviewer_Score"] == 8.0


def test_sorting(sample_data):
    """Verify descending sorting by average score."""

    result = aggregate_by_country(sample_data)

    assert result["Average_Reviewer_Score"].is_monotonic_decreasing


def test_total_reviews_preserved(sample_data):
    """Verify that aggregation preserves total review counts."""

    result = aggregate_by_country(sample_data)

    assert result["Number_of_Reviews"].sum() == len(sample_data)