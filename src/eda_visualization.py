import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# Define a portable output path relative to the project root.
RESULTS_PATH = Path(__file__).resolve().parents[1] / "results"


def plot_eda(df):
    """
    Function: plot_eda

    Purpose:
        Generate exploratory visualizations to understand
        customer satisfaction, geographical distribution
        and temporal trends in the original dataset.

    Input:
        df: pandas DataFrame containing hotel reviews.

    Output:
        None. Saves three PNG visualization files in results/.
    """

    # Create the output directory if it does not exist.
    RESULTS_PATH.mkdir(parents=True, exist_ok=True)

    # Apply a consistent visual style to all charts.
    sns.set_theme(style="whitegrid")

    # --------------------------------------------------
    # 1. Reviewer score distribution
    # --------------------------------------------------

    # A histogram is used to understand the distribution
    # of customer ratings and identify possible skewness.
    # KDE provides a smoothed estimate of the distribution.

    plt.figure(figsize=(10, 6))

    sns.histplot(
        data=df,
        x="Reviewer_Score",
        bins=30,
        kde=True,
        color="steelblue"
    )

    plt.title("Distribution of Hotel Reviewer Scores")
    plt.xlabel("Reviewer Score")
    plt.ylabel("Number of Reviews")
    plt.tight_layout()

    # Save the visualization at high resolution.
    plt.savefig(
        RESULTS_PATH / "reviewer_score_distribution.png",
        dpi=300
    )

    # Close the figure to release memory.
    plt.close()

    # --------------------------------------------------
    # 2. Number of reviews per country
    # --------------------------------------------------

    # Extract countries from hotel addresses because
    # the original dataset has no separate Country column.
    countries = (
        df["Hotel_Address"]
        .str.strip()
        .str.extract(
            r"(United Kingdom|Netherlands|France|Spain|Italy|Austria)$",
            expand=False
        )
    )

    # Count review records associated with each country.
    country_counts = countries.value_counts()

    # A bar chart allows comparison between countries
    # and helps identify geographical imbalances.
    plt.figure(figsize=(10, 6))

    country_counts.plot(
        kind="bar",
        color="steelblue"
    )

    plt.title("Number of Hotel Reviews per Country")
    plt.xlabel("Country")
    plt.ylabel("Number of Reviews")
    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.savefig(
        RESULTS_PATH / "reviews_per_country.png",
        dpi=300
    )

    plt.close()

    # --------------------------------------------------
    # 3. Monthly review trends
    # --------------------------------------------------

    # Convert review dates to datetime format to enable
    # chronological grouping.
    # Invalid dates are converted to NaT.
    dates = pd.to_datetime(
        df["Review_Date"],
        format="%m/%d/%Y",
        errors="coerce"
    )

    # Aggregate reviews by calendar month and sort
    # chronologically to preserve the temporal sequence.
    monthly_counts = (
        dates.dt.to_period("M")
        .value_counts()
        .sort_index()
    )

    # Convert monthly periods into timestamps for plotting.
    monthly_counts.index = monthly_counts.index.to_timestamp()

    # A line chart helps identify changes in review volume,
    # potential seasonality and unusual temporal patterns.
    plt.figure(figsize=(12, 6))

    plt.plot(
        monthly_counts.index,
        monthly_counts.values,
        marker="o",
        color="steelblue"
    )

    plt.title("Monthly Hotel Review Trends")
    plt.xlabel("Date")
    plt.ylabel("Number of Reviews")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        RESULTS_PATH / "monthly_review_trends.png",
        dpi=300
    )

    plt.close()

    print("\n--- EDA VISUALIZATIONS ---")
    print("Three visualizations saved in results/")