import pandas as pd
from pathlib import Path


# Define a portable path for the processed dataset.
# The cleaned CSV is generated locally rather than
# uploaded to GitHub because of its large file size.
PROCESSED_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "processed"
    / "hotel_reviews_cleaned.csv"
)


def clean_data(df):
    """
    Function: clean_data

    Purpose:
        Clean and transform the original hotel reviews
        dataset to provide a consistent foundation for
        the four analytical queries.

    Input:
        df: pandas DataFrame containing raw hotel reviews.

    Output:
        pandas DataFrame containing cleaned hotel reviews
        and two additional variables: Country and Hotel_ID.
    """

    # Work on a copy to preserve the original dataset
    # and avoid unintended modifications.
    df = df.copy()

    # Record the initial number of observations
    # to measure the impact of preprocessing.
    initial_rows = len(df)

    # --------------------------------------------------
    # 1. Remove exact duplicate rows
    # --------------------------------------------------

    # Identical records may lead to double counting
    # and bias review counts and satisfaction indicators.
    # Only exact duplicates across all columns are removed.
    df = df.drop_duplicates().reset_index(drop=True)

    # --------------------------------------------------
    # 2. Convert review dates to datetime
    # --------------------------------------------------

    # The original dates are stored as text.
    # Datetime conversion enables chronological sorting,
    # monthly aggregation and temporal forecasting.
    # Invalid dates become NaT for quality monitoring.
    df["Review_Date"] = pd.to_datetime(
        df["Review_Date"],
        format="%m/%d/%Y",
        errors="coerce"
    )

    # --------------------------------------------------
    # 3. Remove unnecessary spaces
    # --------------------------------------------------

    # Leading and trailing spaces may create inconsistent
    # text values and affect grouping or text analysis.
    # The original meaning of customer reviews is preserved.
    text_columns = [
        "Hotel_Name",
        "Hotel_Address",
        "Reviewer_Nationality",
        "Positive_Review",
        "Negative_Review"
    ]

    for column in text_columns:
        df[column] = df[column].str.strip()

    # --------------------------------------------------
    # 4. Extract hotel country
    # --------------------------------------------------

    # The original dataset has no separate Country column.
    # Extracting countries from hotel addresses enables
    # geographical comparisons and country-level grouping.
    # The pattern covers the six countries in this dataset.
    df["Country"] = df["Hotel_Address"].str.extract(
        r"(United Kingdom|Netherlands|France|Spain|Italy|Austria)$",
        expand=False
    )

    # --------------------------------------------------
    # 5. Create a hotel identifier
    # --------------------------------------------------

    # Hotel names alone are not necessarily unique.
    # Combining name and address helps distinguish hotels
    # with identical names but different locations.
    # This is a dataset-based identifier, not an official ID.
    df["Hotel_ID"] = (
        df["Hotel_Name"] + " | " + df["Hotel_Address"]
    )

    # --------------------------------------------------
    # 6. Preserve missing coordinates
    # --------------------------------------------------

    # Reviews without latitude or longitude remain useful
    # for aggregation, pattern mining and forecasting.
    # Removing them globally would unnecessarily reduce
    # the amount of available information.
    #
    # Missing coordinates will therefore be handled
    # separately during Query 4: spatial clustering.
    #
    # No original columns are removed because different
    # analytical queries may require different features.

    # --------------------------------------------------
    # 7. Validate preprocessing results
    # --------------------------------------------------

    # Report the impact of cleaning and verify whether
    # important data quality issues remain.
    print("\n--- DATA PREPROCESSING ---")
    print(f"Initial rows: {initial_rows}")
    print(f"Removed duplicates: {initial_rows - len(df)}")
    print(f"Remaining rows: {len(df)}")
    print(f"Number of columns: {df.shape[1]}")
    print(f"Invalid dates: {df['Review_Date'].isna().sum()}")
    print(f"Missing countries: {df['Country'].isna().sum()}")
    print(f"Unique hotels: {df['Hotel_ID'].nunique()}")
    print(f"Missing latitude: {df['lat'].isna().sum()}")
    print(f"Missing longitude: {df['lng'].isna().sum()}")

    return df


def save_cleaned_data(df, file_path=PROCESSED_PATH):
    """
    Function: save_cleaned_data

    Purpose:
        Export the cleaned dataset locally so that
        all team members can reproduce the analysis.

    Input:
        df: pandas DataFrame containing cleaned hotel reviews.
        file_path: Destination CSV path.

    Output:
        None. Saves the cleaned dataset as a CSV file.
    """

    # Convert the destination into a Path object
    # to support portable file management.
    file_path = Path(file_path)

    # Create the destination directory if necessary.
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Export without the pandas index because it is
    # not an original or analytical dataset variable.
    df.to_csv(file_path, index=False)

    print("\n--- CLEANED DATASET SAVED ---")
    print(f"Location: {file_path}")