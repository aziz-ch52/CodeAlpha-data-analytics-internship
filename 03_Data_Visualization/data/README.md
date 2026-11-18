# Data Directory - Visualization Phase

This directory stores the datasets used for Task 3 (Data Visualization) of the CodeAlpha internship[cite: 26]. The primary dataset is the cleaned e-commerce transaction data outputted from the Exploratory Data Analysis (EDA) phase.

## Folder Structure

* **`raw/`**: Contains the pre-visualization baseline data imported from the EDA outputs[cite: 26]. 
* **`processed/`**: Contains the final, transformed datasets strictly formatted for dashboard ingestion and visualization scripts (e.g., `cleaned_dataset.csv`).

## Primary Dataset: E-Commerce Transactions

The visual analysis relies on `cleaned_dataset.csv`, which contains structured financial and categorical data. 

### Data Dictionary

| Column Name        | Data Type   | Description                                    | Visualization Use Case                |
|:-------------------|:------------|:-----------------------------------------------|:--------------------------------------|
| `order_id`         | Integer     | Unique identifier for each transaction         | Record counting (Total Orders)        |
| `order_date`       | Date        | Date the order was placed                      | Time-series trends (X-axis)           |
| `product_id`       | Integer     | Unique identifier for the product              | Granular product tracking             |
| `product_category` | Categorical | Category of the product (e.g., Books, Fashion) | Dashboard slicer / Bar chart grouping |
| `price`            | Float       | Original unit price                            | Pricing analysis                      |
| `discount_percent` | Integer     | Discount applied to the item                   | Correlation with sales volume         |
| `quantity_sold`    | Integer     | Number of units purchased                      | Volume aggregation                    |
| `customer_region`  | Categorical | Geographic region of the buyer                 | Map visuals / Geographic filters      |
| `payment_method`   | Categorical | Payment type (e.g., UPI, Credit Card)          | Payment distribution                  |
| `rating`           | Float       | Customer rating (1.0 to 5.0)                   | Quality/Satisfaction KPI              |
| `review_count`     | Integer     | Number of reviews for the product              | Popularity weighting                  |
| `discounted_price` | Float       | Price after applying the discount              | Revenue calculations                  |
| `total_revenue`    | Float       | `discounted_price` * `quantity_sold`           | Primary financial KPI (Y-axis)        |
| `profit`           | Float       | Calculated net profit from the transaction     | Secondary financial KPI               |

## Usage Notes
* Do not perform data cleaning in this directory. If structural data issues are found during visualization, revert to the `02_Exploratory_Data_Analysis` pipeline, fix the source, and re-export the processed file.
* Power BI (`.pbix`) files and Python Notebooks (`.ipynb`) in the parent directory point directly to the files in the `processed/` folder.