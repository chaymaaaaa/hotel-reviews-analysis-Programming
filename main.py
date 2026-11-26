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
    Function: main

    Purpose:
        Execute the hotel reviews analysis pipeline
        following the Knowledge Discovery in Databases
        (KDD) methodology.

    Input:
        None. The dataset is loaded from the project directory.

    Output:
        None. Displays exploratory and analytical results,
        saves the cleaned dataset, exports Query 1 indicators
        and generates visualizations.
    """

    # --------------------------------------------------
    # 1. Data collection
    # --------------------------------------------------

    # Load the original hotel reviews dataset.
    df = load_data()

    # --------------------------------------------------
    # 2. Exploratory data analysis
    # --------------------------------------------------

    # Understand the dataset structure, quality,
    # temporal coverage and geographical distribution.
    explore_data(df)
    analyze_data_quality(df)
    explore_temporal_spatial(df)

    # Generate exploratory visualizations.
    plot_eda(df)

    # --------------------------------------------------
    # 3. Data preprocessing and transformation
    # --------------------------------------------------

    # Prepare a consistent dataset for all analytical queries.
    cleaned_df = clean_data(df)

    # Save the cleaned dataset for reproducibility.
    save_cleaned_data(cleaned_df)

    # --------------------------------------------------
    # 4. Query 1: Grouping and aggregation
    # --------------------------------------------------

    # Calculate country-level analytical indicators.
    country_summary = aggregate_by_country(cleaned_df)

    # Export the analytical results.
    save_aggregation_results(country_summary)

    # --------------------------------------------------
    # 5. Visualization and interpretation
    # --------------------------------------------------

    # Generate charts to support interpretation of Query 1.
    plot_country_summary(country_summary)

    # Queries 2, 3 and 4 and the interactive dashboard
    # will be integrated after their respective modules
    # have been completed and validated.


# Execute the pipeline only when this file is run directly.
# Importing this module does not automatically run the analysis.
if __name__ == "__main__":
    main()