import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


RESULTS_PATH = Path(__file__).resolve().parents[1] / "results"


def plot_eda(df):
    """
    Generate and save exploratory data visualizations.

    Input:
        df: pandas DataFrame containing hotel reviews.

    Output:
        None. Saves three visualization files in results/.
    """

    RESULTS_PATH.mkdir(parents=True, exist_ok=True)

    sns.set_theme(style="whitegrid")

    # 1. Reviewer score distribution
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

    plt.savefig(
        RESULTS_PATH / "reviewer_score_distribution.png",
        dpi=300
    )

    plt.close()

    # 2. Number of reviews per country
    countries = (
        df["Hotel_Address"]
        .str.strip()
        .str.extract(
            r"(United Kingdom|Netherlands|France|Spain|Italy|Austria)$",
            expand=False
        )
    )

    country_counts = countries.value_counts()

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

    # 3. Monthly review trends
    dates = pd.to_datetime(
        df["Review_Date"],
        format="%m/%d/%Y",
        errors="coerce"
    )

    monthly_counts = (
        dates.dt.to_period("M")
        .value_counts()
        .sort_index()
    )

    monthly_counts.index = monthly_counts.index.to_timestamp()

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