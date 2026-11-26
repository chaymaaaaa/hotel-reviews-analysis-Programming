import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


RESULTS_PATH = Path(__file__).resolve().parents[1] / "results"


def plot_country_summary(country_summary):
    """
    Generate visualizations for Query 1.

    Input:
        country_summary: pandas DataFrame containing
        country-level aggregation results.

    Output:
        None. Saves three analytical charts in results/.
    """

    RESULTS_PATH.mkdir(parents=True, exist_ok=True)

    sns.set_theme(style="whitegrid")

    # 1. Average reviewer score by country
    plt.figure(figsize=(10, 6))

    ax = sns.barplot(
        data=country_summary,
        x="Country",
        y="Average_Reviewer_Score",
        color="steelblue"
    )

    ax.bar_label(ax.containers[0], fmt="%.2f")

    plt.title("Average Customer Satisfaction by Country")
    plt.xlabel("Country")
    plt.ylabel("Average Reviewer Score")
    plt.ylim(0, 10)
    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.savefig(
        RESULTS_PATH / "q1_average_score_by_country.png",
        dpi=300
    )

    plt.close()

    # 2. Number of hotels by country
    hotel_summary = country_summary.sort_values(
        "Number_of_Hotels",
        ascending=False
    )

    plt.figure(figsize=(10, 6))

    ax = sns.barplot(
        data=hotel_summary,
        x="Country",
        y="Number_of_Hotels",
        color="steelblue"
    )

    ax.bar_label(ax.containers[0], fmt="%d")

    plt.title("Number of Hotels per Country")
    plt.xlabel("Country")
    plt.ylabel("Number of Hotels")
    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.savefig(
        RESULTS_PATH / "q1_hotels_by_country.png",
        dpi=300
    )

    plt.close()

    # 3. Review volume versus satisfaction
    plt.figure(figsize=(11, 6))

    sns.scatterplot(
        data=country_summary,
        x="Number_of_Reviews",
        y="Average_Reviewer_Score",
        hue="Country",
        s=150
    )

    plt.title("Review Volume vs Customer Satisfaction")
    plt.xlabel("Number of Reviews")
    plt.ylabel("Average Reviewer Score")
    plt.legend(title="Country")
    plt.tight_layout()

    plt.savefig(
        RESULTS_PATH / "q1_reviews_vs_satisfaction.png",
        dpi=300
    )

    plt.close()

    print("\n--- QUERY 1 VISUALIZATIONS ---")
    print("Three aggregation charts saved in results/")