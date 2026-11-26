import pandas as pd
from pathlib import Path


# Build the dataset path relative to the project root
# instead of using a machine-specific absolute path.
# This makes the project portable across team members.
DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "raw"
    / "Hotel_Reviews.csv"
)


def load_data(file_path=DATA_PATH):
    """
    Function: load_data

    Purpose:
        Load the original hotel reviews dataset.

    Input:
        file_path: Path to the CSV dataset.

    Output:
        pandas DataFrame containing the original hotel reviews.
    """

    # Read the CSV file into a pandas DataFrame.
    df = pd.read_csv(file_path)

    return df


def explore_data(df):
    """
    Function: explore_data

    Purpose:
        Understand the initial structure and characteristics
        of the dataset before preprocessing.

    Input:
        df: pandas DataFrame containing hotel reviews.

    Output:
        None. Displays dimensions, columns, data types
        and the first five rows.
    """

    # Identify the number of observations and variables.
    print("\n--- DATASET DIMENSIONS ---")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")

    # Identify the available features.
    print("\n--- COLUMN NAMES ---")
    print(df.columns.tolist())

    # Check data types to identify variables requiring conversion.
    print("\n--- DATA TYPES ---")
    print(df.dtypes)

    # Inspect a sample of the original observations.
    print("\n--- FIRST FIVE ROWS ---")
    print(df.head())


def analyze_data_quality(df):
    """
    Function: analyze_data_quality

    Purpose:
        Identify data quality issues before cleaning
        and analytical processing.

    Input:
        df: pandas DataFrame containing hotel reviews.

    Output:
        None. Displays missing values, missing percentages,
        duplicate rows and numerical descriptive statistics.
    """

    # Identify missing values in each variable.
    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())

    # Calculate percentages to evaluate the relative
    # importance of missing data.
    print("\n--- MISSING VALUES PERCENTAGE ---")
    missing_percentage = df.isnull().mean() * 100
    print(missing_percentage.round(2))

    # Identify exact duplicates that could bias
    # review counts and satisfaction indicators.
    print("\n--- DUPLICATE ROWS ---")
    print(f"Number of duplicates: {df.duplicated().sum()}")

    # Examine numerical distributions, including
    # means, standard deviations, quartiles and ranges.
    print("\n--- NUMERICAL DESCRIPTIVE STATISTICS ---")
    print(df.describe().T.round(2).to_string())


def explore_temporal_spatial(df):
    """
    Function: explore_temporal_spatial

    Purpose:
        Understand the temporal and geographical coverage
        of the dataset before forecasting and spatial analysis.

    Input:
        df: pandas DataFrame containing hotel reviews.

    Output:
        None. Displays date ranges, invalid dates,
        distinct hotel names and geographical distribution.
    """

    print("\n--- TEMPORAL COVERAGE ---")

    # Convert dates temporarily for exploratory analysis.
    # Invalid dates become NaT so they can be identified
    # without interrupting the analysis.
    # The original DataFrame is not modified.
    dates = pd.to_datetime(
        df["Review_Date"],
        format="%m/%d/%Y",
        errors="coerce"
    )

    # Identify the available historical period.
    print(f"First review date: {dates.min()}")
    print(f"Last review date: {dates.max()}")
    print(f"Invalid dates: {dates.isna().sum()}")

    # Count distinct calendar months represented in the data.
    print(f"Number of months: {dates.dt.to_period('M').nunique()}")

    print("\n--- HOTEL INFORMATION ---")

    # Count distinct hotel names.
    # This is not necessarily the number of distinct hotels,
    # because different hotels may share the same name.
    print(f"Distinct hotel names: {df['Hotel_Name'].nunique()}")

    print("\n--- GEOGRAPHICAL COVERAGE ---")

    # The original dataset does not contain a Country column.
    # Extract country names from the end of hotel addresses.
    # Include United Kingdom as a complete country name.
    countries = (
        df["Hotel_Address"]
        .str.strip()
        .str.extract(
            r"(United Kingdom|Netherlands|France|Spain|Italy|Austria)$",
            expand=False
        )
    )

    # Identify the number of countries represented.
    print(f"Number of countries: {countries.nunique()}")

    # Evaluate the geographical distribution of reviews
    # and identify possible country-level imbalances.
    print("\nNumber of reviews per country:")
    print(countries.value_counts())

    # Verify whether any hotel address could not be classified.
    print(f"\nUnidentified countries: {countries.isna().sum()}")