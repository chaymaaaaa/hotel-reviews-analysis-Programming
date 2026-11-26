from src.data_preparation import (
    load_data,
    explore_data,
    analyze_data_quality,
    explore_temporal_spatial
)

from src.eda_visualization import plot_eda

from src.preprocessing import (
    clean_data,
    save_cleaned_data
)

from src.aggregation import (
    aggregate_by_country,
    save_aggregation_results
)

from src.aggregation_visualization import plot_country_summary


def main():
    """
    Execute the hotel reviews analysis pipeline.

    Input:
        None.

    Output:
        None. Executes EDA, preprocessing, Query 1
        and analytical visualizations.
    """

    # Load raw dataset
    df = load_data()

    # Exploratory data analysis
    explore_data(df)
    analyze_data_quality(df)
    explore_temporal_spatial(df)
    plot_eda(df)

    # Data preprocessing
    cleaned_df = clean_data(df)
    save_cleaned_data(cleaned_df)

    # Query 1: Grouping and aggregation
    country_summary = aggregate_by_country(cleaned_df)
    save_aggregation_results(country_summary)

    # Query 1 visualizations
    plot_country_summary(country_summary)


if __name__ == "__main__":
    main()