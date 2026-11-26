### Dataset Source and Description

The dataset used in this project is **515K Hotel Reviews Data in Europe**, published by Jiashen Liu on Kaggle.

**Source:** https://www.kaggle.com/datasets/jiashenliu/515k-hotel-reviews-data-in-europe

The dataset contains 515,738 hotel review records and 17 original variables. It covers hotels located in Austria, France, Italy, the Netherlands, Spain and the United Kingdom.

The reviews were collected between August 4, 2015, and August 3, 2017.

### Justification of Dataset Selection

The dataset was selected because it supports three complementary analytical dimensions:

- **Temporal dimension:** Review dates enable time-series analysis and forecasting.
- **Spatial dimension:** Hotel addresses, latitude and longitude enable geographical analysis and spatial clustering.
- **Analytical dimension:** Customer ratings and textual reviews enable statistical aggregation, customer satisfaction analysis and frequent pattern mining.

The dataset is particularly relevant to the hospitality industry because it provides insights into customer satisfaction, recurring customer preferences, review activity and geographical differences.

### Data Availability and Reproducibility

Due to its large file size, the original dataset is not stored directly in the GitHub repository.

To reproduce the analysis, download `Hotel_Reviews.csv` from the Kaggle source and place it in:

`data/raw/Hotel_Reviews.csv`

The preprocessing pipeline automatically generates the cleaned dataset in:

`data/processed/hotel_reviews_cleaned.csv`