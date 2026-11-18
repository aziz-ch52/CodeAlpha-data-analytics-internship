# Exploratory Data Analysis: E-Commerce Retail Transactions

This folder contains the datasets, notebooks, and findings for the Exploratory Data Analysis (EDA) phase of the CodeAlpha Data Analytics Internship. 

The primary cleaned dataset analyzed in this phase is **ecommerce_retail_transactions_synthetic cleaned.xlsx**.

## Objective
The goal of this EDA is to investigate customer purchasing behavior, analyze product profitability, and identify trends across different demographics and geographic regions to inform business strategy.

## File Details
* **File Name:** `ecommerce_retail_transactions_synthetic cleaned.xlsx`
* **Format:** Microsoft Excel Spreadsheet (.xlsx)
* **Status:** Cleaned (Missing values handled, data types standardized, duplicates removed).
* **Location:** `/02_Exploratory_Data_Analysis/data/processed/`

## Data Dictionary

| Column Name           | Data Type | Description                                               |
|:----------------------|:----------|:----------------------------------------------------------|
| `Order_ID`            | String    | Unique identifier for each transaction.                   |
| `Order_Date`          | Date/Time | Date when the order was placed.                           |
| `Customer_ID`         | String    | Unique identifier for the purchasing customer.            |
| `Customer_Age`        | Integer   | Age of the customer.                                      |
| `Gender`              | String    | Gender of the customer.                                   |
| `City`                | String    | City where the order was shipped/placed.                  |
| `State`               | String    | State where the order was shipped/placed.                 |
| `Customer_Segment`    | String    | Categorization of the customer (e.g., Premium, Standard). |
| `Product_ID`          | String    | Unique identifier for the purchased product.              |
| `Product_Name`        | String    | Name of the purchased product.                            |
| `Category`            | String    | High-level grouping of the product.                       |
| `Sub_Category`        | String    | Granular grouping of the product.                         |
| `Unit_Price`          | Integer   | Original price of a single product unit.                  |
| `Quantity`            | Integer   | Number of units purchased in the transaction.             |
| `Discount_Percentage` | Integer   | Discount applied to the order.                            |
| `Total_Sales`         | Float     | Total revenue generated from the transaction.             |
| `Payment_Method`      | String    | Method used to pay for the order.                         |
| `Order_Status`        | String    | Current status of the order (e.g., Delivered, Cancelled). |
| `Shipping_Days`       | Integer   | Number of days taken to ship the order.                   |
| `Profit`              | Float     | Net profit generated from the transaction.                |

## Key Analytical Workflows
1. **Univariate Analysis:** Distribution of `Customer_Age`, `Total_Sales`, and `Profit` to identify outliers.
2. **Bivariate/Multivariate Analysis:** Evaluating `Profit` margins across `Category` and `Customer_Segment`.
3. **Time-Series Exploration:** Tracking `Total_Sales` trends over time using `Order_Date`.
4. **Geographic Distribution:** Identifying high-performing `State` and `City` locations.

## Usage Notes
* This file represents the **final, cleaned state** of the raw data.
* Do not perform further data cleaning operations on `ecommerce_retail_transactions_synthetic cleaned.xlsx`. Any required structural changes must be made to the raw data pipeline in the Jupyter Notebook and re-exported.
* This dataset serves as the single source of truth for the subsequent Data Visualization phase.