import pandas as pd
from pathlib import Path


PROCESSED_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "processed"
    / "hotel_reviews_cleaned.csv"
)


def clean_data(df):
    """
    Clean and transform the hotel reviews dataset.

    Input:
        df: pandas DataFrame containing raw hotel reviews.

    Output:
        pandas DataFrame containing cleaned hotel reviews.
    """

    df = df.copy()

    initial_rows = len(df)

    # 1. Remove exact duplicate rows
    df = df.drop_duplicates().reset_index(drop=True)

    # 2. Convert review dates to datetime
    df["Review_Date"] = pd.to_datetime(
        df["Review_Date"],
        format="%m/%d/%Y",
        errors="coerce"
    )

    # 3. Remove unnecessary spaces
    text_columns = [
        "Hotel_Name",
        "Hotel_Address",
        "Reviewer_Nationality",
        "Positive_Review",
        "Negative_Review"
    ]

    for column in text_columns:
        df[column] = df[column].str.strip()

    # 4. Extract hotel country
    df["Country"] = df["Hotel_Address"].str.extract(
        r"(United Kingdom|Netherlands|France|Spain|Italy|Austria)$",
        expand=False
    )

    # 5. Create a hotel identifier
    df["Hotel_ID"] = (
        df["Hotel_Name"] + " | " + df["Hotel_Address"]
    )

    # 6. Preserve missing coordinates
    # They will be handled separately for spatial clustering.

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
    Save the cleaned dataset locally.

    Input:
        df: pandas DataFrame containing cleaned hotel reviews.
        file_path: destination CSV path.

    Output:
        None. Saves the cleaned dataset as a CSV file.
    """

    file_path = Path(file_path)

    file_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(file_path, index=False)

    print("\n--- CLEANED DATASET SAVED ---")
    print(f"Location: {file_path}")