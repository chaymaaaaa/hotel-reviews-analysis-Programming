from pathlib import Path


# Define a portable directory for analytical results.
RESULTS_PATH = Path(__file__).resolve().parents[1] / "results"


def aggregate_by_country(df):
    """
    Function: aggregate_by_country

    Purpose:
        Answer Query 1 by comparing customer satisfaction
        and review activity across the six European countries
        represented in the dataset.

    Input:
        df: pandas DataFrame containing cleaned hotel reviews,
        including Country, Hotel_ID and Reviewer_Score.

    Output:
        pandas DataFrame containing four country-level
        analytical indicators:
        - Number of reviews
        - Number of distinct hotel identifiers
        - Average reviewer score
        - Median reviewer score
    """

    # Group observations according to the country
    # where each hotel is located.
    #
    # Number_of_Reviews:
    # Measures the volume of review records per country.
    #
    # Number_of_Hotels:
    # Counts distinct hotel name-address identifiers
    # rather than counting the same hotel repeatedly.
    #
    # Average_Reviewer_Score:
    # Measures average customer satisfaction.
    # Each individual review has equal weight.
    #
    # Median_Reviewer_Score:
    # Provides a measure of central tendency that is
    # less sensitive to extreme ratings than the mean.

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

    # Sort countries by average customer satisfaction
    # to facilitate comparison between countries.
    country_summary = country_summary.sort_values(
        by="Average_Reviewer_Score",
        ascending=False
    ).reset_index(drop=True)

    # Round numerical results to two decimal places
    # to improve readability.
    # Sorting is performed before rounding.
    country_summary = country_summary.round(2)

    # Display the analytical results for verification.
    print("\n--- QUERY 1: COUNTRY AGGREGATION ---")
    print(country_summary.to_string(index=False))

    return country_summary


def save_aggregation_results(country_summary):
    """
    Function: save_aggregation_results

    Purpose:
        Export Query 1 results for reproducibility,
        visualization and dashboard integration.

    Input:
        country_summary: pandas DataFrame containing
        country-level analytical indicators.

    Output:
        None. Saves country_summary.csv in results/.
    """

    # Create the results directory if necessary.
    RESULTS_PATH.mkdir(parents=True, exist_ok=True)

    # Define the destination of the analytical results.
    output_path = RESULTS_PATH / "country_summary.csv"

    # Export without the pandas index because it is
    # not an analytical indicator.
    country_summary.to_csv(output_path, index=False)

    print("\n--- QUERY 1 RESULTS SAVED ---")
    print(f"Location: {output_path}")