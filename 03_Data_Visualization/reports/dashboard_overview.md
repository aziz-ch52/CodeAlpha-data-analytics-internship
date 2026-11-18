# Power BI Dashboard Overview

## Purpose
This interactive dashboard synthesizes global e-commerce sales data to provide executive stakeholders with a real-time view of revenue health, categorical performance, and purchasing trends.

## Data Lineage
* **Source:** `global_ecommerce_sales.csv`
* **Dataset Shape:** 50,000 rows across 14 columns (`order_id`, `order_date`, `product_id`, `product_category`, `price`, `discount_percent`, `quantity_sold`, `customer_region`, `payment_method`, `rating`, `review_count`, `discounted_price`, `total_revenue`, `profit`).
* **Processing:** Cleaned and standardized via Python (Pandas), dropping exact duplicates and standardizing date formats to preserve distribution integrity.

## Key Pages & Layout
1. **Executive Summary:** High-level KPIs (Total Revenue, Total Quantity Sold, Average Order Value). Features the Monthly Revenue Trend line chart.
2. **Category Deep-Dive:** Focuses on product-level performance across the `product_category` feature. Highlights the Revenue Distribution Boxplot to spot Home & Kitchen outliers versus the high-volume Beauty segment.
3. **Correlation & Drivers:** A diagnostic page showing the correlation heatmap to help analysts understand the mathematical relationships between `discount_percent`, `quantity_sold`, and `total_revenue`.

## Interactive Elements
* **Global Date Slicer:** Allows stakeholders to filter all metrics by specific financial quarters based on `order_date`.
* **Category Filters:** Enables deep-dives into specific product segments (e.g., Beauty, Home & Kitchen) to isolate performance drivers.
