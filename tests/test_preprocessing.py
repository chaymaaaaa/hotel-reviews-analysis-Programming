import pandas as pd
import pytest

from src.preprocessing import clean_data


@pytest.fixture
def sample_data():
    """
    Create a small dataset for preprocessing tests.

    Input:
        None.

    Output:
        pandas DataFrame containing sample hotel reviews.
    """

    return pd.DataFrame({
        "Hotel_Name": [
            "Grand Hotel",
            "Grand Hotel",
            "Grand Hotel"
        ],
        "Hotel_Address": [
            "London United Kingdom",
            "London United Kingdom",
            "Paris France"
        ],
        "Review_Date": [
            "8/4/2015",
            "8/4/2015",
            "8/5/2015"
        ],
        "Reviewer_Nationality": [
            " British ",
            " British ",
            " French "
        ],
        "Positive_Review": [
            "Good hotel",
            "Good hotel",
            "Excellent service"
        ],
        "Negative_Review": [
            "No Negative",
            "No Negative",
            "Small room"
        ],
        "Reviewer_Score": [8.0, 8.0, 9.0],
        "lat": [51.5, 51.5, None],
        "lng": [-0.1, -0.1, None]
    })


def test_remove_duplicates(sample_data):
    """Verify that exact duplicate rows are removed."""

    cleaned = clean_data(sample_data)

    assert len(cleaned) == 2


def test_date_conversion(sample_data):
    """Verify that review dates are converted to datetime."""

    cleaned = clean_data(sample_data)

    assert pd.api.types.is_datetime64_any_dtype(
        cleaned["Review_Date"]
    )

    assert cleaned["Review_Date"].isna().sum() == 0


def test_country_extraction(sample_data):
    """Verify that countries are correctly extracted."""

    cleaned = clean_data(sample_data)

    assert set(cleaned["Country"]) == {
        "United Kingdom",
        "France"
    }


def test_hotel_identification(sample_data):
    """Verify that hotels with different addresses are distinct."""

    cleaned = clean_data(sample_data)

    assert cleaned["Hotel_ID"].nunique() == 2


def test_missing_coordinates(sample_data):
    """Verify that missing coordinates are preserved."""

    cleaned = clean_data(sample_data)

    assert cleaned["lat"].isna().sum() == 1
    assert cleaned["lng"].isna().sum() == 1


def test_text_cleaning(sample_data):
    """Verify that unnecessary spaces are removed."""

    cleaned = clean_data(sample_data)

    assert cleaned["Reviewer_Nationality"].tolist() == [
        "British",
        "French"
    ]


def test_original_data_unchanged(sample_data):
    """Verify that preprocessing does not modify raw data."""

    original = sample_data.copy(deep=True)

    clean_data(sample_data)

    pd.testing.assert_frame_equal(sample_data, original)