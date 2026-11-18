# Power BI DAX Measures Documentation

This document serves as the data dictionary for all calculated measures used in the `CodeAlpha_Dashboard.pbix` file. These measures are built on top of the `cleaned_ecommerce_sales` table to power the executive KPIs and visualizations.

---

## 💰 Core Financial KPIs

### 1. Total Revenue
```dax
Total Revenue = SUM(cleaned_ecommerce_sales[total_revenue])
```
* **Description:** Aggregates the total top-line revenue across all filtered transactions.
* **Formatting:** Currency (`$`), 2 Decimal Places.

### 2. Total Profit
```dax
Total Profit = SUM(cleaned_ecommerce_sales[profit])
```
* **Description:** Aggregates the net profit after discounts and base costs are applied.
* **Formatting:** Currency (`$`), 2 Decimal Places.

### 3. Profit Margin %
```dax
Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)
```
* **Description:** Calculates the ratio of profit to total revenue. The `DIVIDE` function safely handles potential division by zero.
* **Formatting:** Percentage (`%`), 2 Decimal Places.

---

## 📦 Operational & Volume KPIs

### 4. Total Orders
```dax
Total Orders = DISTINCTCOUNT(cleaned_ecommerce_sales[order_id])
```
* **Description:** Counts the unique number of transactions. Using `DISTINCTCOUNT` instead of `COUNTROWS` ensures multi-item orders are not double-counted as separate transactions.
* **Formatting:** Whole Number, Comma Separated.

### 5. Total Items Sold
```dax
Total Items Sold = SUM(cleaned_ecommerce_sales[quantity_sold])
```
* **Description:** Aggregates the absolute volume of physical products moved.
* **Formatting:** Whole Number, Comma Separated.

### 6. Average Order Value (AOV)
```dax
AOV = DIVIDE([Total Revenue], [Total Orders], 0)
```
* **Description:** Calculates the average dollar amount spent each time a customer places an order. This is a critical metric for evaluating the discount strategy.
* **Formatting:** Currency (`$`), 2 Decimal Places.

---

## ⭐ Customer Satisfaction

### 7. Average Rating
```dax
Average Rating = AVERAGE(cleaned_ecommerce_sales[rating])
```
* **Description:** Calculates the mean customer rating across the filtered context.
* **Formatting:** Decimal Number, 1 Decimal Place.
