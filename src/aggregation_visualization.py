import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# Define a portable directory for visualization outputs.
RESULTS_PATH = Path(__file__).resolve().parents[1] / "results"


def plot_country_summary(country_summary):
    """
    Function: plot_country_summary

    Purpose:
        Visualize Query 1 results to compare customer
        satisfaction, hotel representation and review
        activity across the six European countries.

    Input:
        country_summary: pandas DataFrame containing
        country-level aggregation results.

    Output:
        None. Saves three analytical PNG charts in results/.
    """

    # Create the output directory if necessary.
    RESULTS_PATH.mkdir(parents=True, exist_ok=True)

    # Apply a consistent visual style across all charts.
    sns.set_theme(style="whitegrid")

    # --------------------------------------------------
    # 1. Average reviewer score by country
    # --------------------------------------------------

    # A bar chart facilitates comparison of average
    # customer satisfaction between countries.
    plt.figure(figsize=(10, 6))

    ax = sns.barplot(
        data=country_summary,
        x="Country",
        y="Average_Reviewer_Score",
        color="steelblue"
    )

    # Display numerical values for easier comparison.
    ax.bar_label(ax.containers[0], fmt="%.2f")

    plt.title("Average Customer Satisfaction by Country")
    plt.xlabel("Country")
    plt.ylabel("Average Reviewer Score")

    # Use a zero-based axis extending to the maximum
    # possible score to avoid exaggerating differences.
    plt.ylim(0, 10)

    plt.xticks(rotation=30)
    plt.tight_layout()

    # Save the chart at high resolution.
    plt.savefig(
        RESULTS_PATH / "q1_average_score_by_country.png",
        dpi=300
    )

    # Release memory after saving the figure.
    plt.close()

    # --------------------------------------------------
    # 2. Number of hotels by country
    # --------------------------------------------------

    # Sort countries by the number of distinct hotel
    # identifiers to make comparisons easier.
    hotel_summary = country_summary.sort_values(
        "Number_of_Hotels",
        ascending=False
    )

    # A bar chart is appropriate for comparing
    # discrete counts across geographical categories.
    plt.figure(figsize=(10, 6))

    ax = sns.barplot(
        data=hotel_summary,
        x="Country",
        y="Number_of_Hotels",
        color="steelblue"
    )

    # Display hotel counts as integer values.
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

    # --------------------------------------------------
    # 3. Review volume versus satisfaction
    # --------------------------------------------------

    # A scatter plot allows exploratory comparison
    # between two numerical indicators:
    # review volume and average customer satisfaction.
    #
    # Each point represents one country.
    # Different colors identify the countries.
    #
    # This visualization is descriptive and does not
    # establish a causal relationship between variables.

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

    # Confirm successful generation of analytical charts.
    print("\n--- QUERY 1 VISUALIZATIONS ---")
    print("Three aggregation charts saved in results/")