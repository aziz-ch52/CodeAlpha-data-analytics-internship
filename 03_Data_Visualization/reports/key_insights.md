# Key Analytical Insights

## 1. Temporal Revenue Trends
* **Visual Reference:** `monthly_revenue_trend.png`
* **Observation:** Global revenue exhibits steady seasonality, peaking in **January 2023 (2023-01)** at approximately **$1,464,174.99**.
* **Significance:** This indicates strong early-year purchasing behavior, which dictates when inventory and marketing budgets should be scaled to maximize returns.

## 2. Categorical Revenue Distribution
* **Visual Reference:** `revenue_by_category_boxplot.png`
* **Observation:** The **Beauty** category drives the highest total volume of revenue. However, the **Home & Kitchen** segment shows the highest variance, containing massive outlier transactions.
* **Significance:** We have a stable, high-volume baseline of revenue from Beauty, but our "whale" clients (the extreme high-value outliers) are primarily purchasing from Home & Kitchen.

## 3. Feature Correlations
* **Visual Reference:** `correlation_heatmap.png`
* **Observation:** `total_revenue` has a moderate positive correlation with `quantity_sold` (**r = 0.59**), but shows virtually zero correlation with customer `rating`. 
* **Significance:** Customer satisfaction (ratings) does not mathematically drive transaction size in this dataset. Volume (quantity) and unit price are the sole statistical drivers of top-line revenue.
