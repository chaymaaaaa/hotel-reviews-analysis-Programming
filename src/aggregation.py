from pathlib import Path


RESULTS_PATH = Path(__file__).resolve().parents[1] / "results"


def aggregate_by_country(df):
    """
    Analyze customer satisfaction by hotel country.

    Input:
        df: pandas DataFrame containing cleaned hotel reviews.

    Output:
        pandas DataFrame containing country-level statistics,
        including review counts, hotel counts, mean scores
        and median scores.
    """

    country_summary = (
        df.groupby("Country")
        .agg(
            Number_of_Reviews=("Reviewer_Score", "size"),
            Number_of_Hotels=("Hotel_ID", "nunique"),
            Average_Reviewer_Score=("Reviewer_Score", "mean"),
            Median_Reviewer_Score=("Reviewer_Score", "median")
        )
        .reset_index()
    )

    country_summary = country_summary.sort_values(
        by="Average_Reviewer_Score",
        ascending=False
    ).reset_index(drop=True)

    country_summary = country_summary.round(2)

    print("\n--- QUERY 1: COUNTRY AGGREGATION ---")
    print(country_summary.to_string(index=False))

    return country_summary


def save_aggregation_results(country_summary):
    """
    Save country-level aggregation results.

    Input:
        country_summary: pandas DataFrame containing
        country-level statistics.

    Output:
        None. Saves the aggregation results as a CSV file.
    """

    RESULTS_PATH.mkdir(parents=True, exist_ok=True)

    output_path = RESULTS_PATH / "country_summary.csv"

    country_summary.to_csv(output_path, index=False)

    print("\n--- QUERY 1 RESULTS SAVED ---")
    print(f"Location: {output_path}")