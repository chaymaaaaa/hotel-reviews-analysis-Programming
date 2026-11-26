import pandas as pd
from pathlib import Path


DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "raw"
    / "Hotel_Reviews.csv"
)


def load_data(file_path=DATA_PATH):
    """
    Load the hotel reviews dataset.

    Input:
        file_path: Path to the CSV dataset.

    Output:
        pandas DataFrame containing the original hotel reviews.
    """
    df = pd.read_csv(file_path)
    return df


def explore_data(df):
    """
    Display the initial structure of the dataset.

    Input:
        df: pandas DataFrame containing hotel reviews.

    Output:
        None. Displays dimensions, columns, data types
        and the first five rows.
    """
    print("\n--- DATASET DIMENSIONS ---")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")

    print("\n--- COLUMN NAMES ---")
    print(df.columns.tolist())

    print("\n--- DATA TYPES ---")
    print(df.dtypes)

    print("\n--- FIRST FIVE ROWS ---")
    print(df.head())


def analyze_data_quality(df):
    """
    Analyze the quality of the hotel reviews dataset.

    Input:
        df: pandas DataFrame containing hotel reviews.

    Output:
        None. Displays missing values, missing percentages,
        duplicate rows and numerical descriptive statistics.
    """
    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())

    print("\n--- MISSING VALUES PERCENTAGE ---")
    missing_percentage = df.isnull().mean() * 100
    print(missing_percentage.round(2))

    print("\n--- DUPLICATE ROWS ---")
    print(f"Number of duplicates: {df.duplicated().sum()}")

    print("\n--- NUMERICAL DESCRIPTIVE STATISTICS ---")
    print(df.describe().T.round(2).to_string())


def explore_temporal_spatial(df):
    """
    Explore the temporal and geographical coverage.

    Input:
        df: pandas DataFrame containing hotel reviews.

    Output:
        None. Displays date ranges, invalid dates,
        hotel counts and geographical distribution.
    """
    print("\n--- TEMPORAL COVERAGE ---")

    dates = pd.to_datetime(
        df["Review_Date"],
        format="%m/%d/%Y",
        errors="coerce"
    )

    print(f"First review date: {dates.min()}")
    print(f"Last review date: {dates.max()}")
    print(f"Invalid dates: {dates.isna().sum()}")
    print(f"Number of months: {dates.dt.to_period('M').nunique()}")

    print("\n--- HOTEL INFORMATION ---")
    print(f"Distinct hotel names: {df['Hotel_Name'].nunique()}")

    print("\n--- GEOGRAPHICAL COVERAGE ---")

    countries = (
        df["Hotel_Address"]
        .str.strip()
        .str.extract(
            r"(United Kingdom|Netherlands|France|Spain|Italy|Austria)$",
            expand=False
        )
    )

    print(f"Number of countries: {countries.nunique()}")

    print("\nNumber of reviews per country:")
    print(countries.value_counts())

    print(f"\nUnidentified countries: {countries.isna().sum()}")