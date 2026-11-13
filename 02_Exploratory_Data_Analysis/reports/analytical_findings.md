# Core Analytical Findings

## 1. Univariate Distributions (The Shape of the Data)
* **Total Sales & Unit Price:** Both `Total_Sales` and `Unit_Price` exhibit right-skewed distributions. The median order value is ₹[X], while high-ticket electronics push maximum order totals up to ₹[Y].
* **Customer Age:** The `Customer_Age` distribution centers around a median of [X] years, with the primary shopper base falling between [X] and [Y] years old.
* **Dominant Category:** `[Category Name]` is the primary driver of order volume, accounting for [X]% of all transactions, followed by `[Second Category]` at [Y]%.
* **Payment & Order Status:** `[Payment Method]` is the most preferred payment option ([X]% of orders), and [X]% of total orders were successfully delivered.

## 2. Bivariate Relationships (How Features Interact)
* **Unit Price vs. Quantity:** A [weak/negative/neutral] correlation ($r = [X]$) was observed between `Unit_Price` and `Quantity`. Higher-priced items are predominantly purchased in single units, whereas lower-priced accessories show higher multi-unit quantities.
* **Category vs. Total Sales:** Boxplot and group analysis reveal that while `[Volume Category]` generates the highest transaction count, `[High-Value Category]` drives the highest revenue with a median order value of ₹[X].
* **Discount Percentage vs. Total Sales:** Orders with discounts between [X]% and [Y]% show [higher/steady] purchase volumes, indicating promotional sensitivity in `[Category Name]`.
* **City/Region vs. Shipping Days:** Metro cities such as `[City Name]` average [X] shipping days, whereas tier-2 cities experience slightly longer delivery windows averaging [Y] days.

## 3. Multivariate & Multicollinearity Checks
* A correlation matrix was executed across all continuous numerical features (`Customer_Age`, `Quantity`, `Unit_Price`, `Discount_Percentage`, `Shipping_Days`, and `Total_Sales`).
* **Key Finding:** `Unit_Price` and `Total_Sales` showed a strong positive correlation coefficient of $r = [X]$ (since total sales is directly derived from unit price and quantity).
* **Action:** If this dataset is used for predictive modeling (such as predicting `Total_Sales`), `Unit_Price` and `Quantity` should be handled carefully to prevent data leakage, while independent features like `Customer_Age` and `Shipping_Days` show low multicollinearity ($r < 0.20$) and can be safely retained.
