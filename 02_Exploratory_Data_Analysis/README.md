# E-Commerce Retail Transactions: Exploratory Data Analysis (EDA)

## 📌 Project Overview
This repository contains a comprehensive Exploratory Data Analysis (EDA) pipeline for e-commerce retail transaction data. Developed as part of a **Data Analytics Internship at CodeAlpha**, this project demonstrates a structured approach to transforming raw, messy data into clean, actionable business insights.

The analysis progresses through a strict pipeline: initial data profiling, rigorous data cleaning, univariate/bivariate/multivariate statistical analysis, and final feature engineering.

---

## 🗂️ Project Structure
The repository is organized following industry-standard data science principles to ensure reproducibility and modularity:

```text
02_Exploratory_Data_Analysis/
│
├── data/                  # Immutable data storage
│   ├── raw/               # Original, unmodified datasets (DO NOT EDIT)
│   └── processed/         # Cleaned, standardized data ready for analysis
│
├── notebooks/             # Sequential Jupyter Notebooks for analysis
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_univariate_analysis.ipynb
│   ├── 04_bivariate_analysis.ipynb
│   ├── 05_multivariate_analysis.ipynb
│   └── 06_final_eda.ipynb
│
├── outputs/               # Generated charts, summary tables, and cleaned exports
│   ├── charts/
│   ├── tables/
│   └── cleaned_data/
│
├── reports/               # Markdown summaries of findings for stakeholders
│   ├── data_quality_report.md
│   ├── analytical_findings.md
│   └── final_summary.md
│
├── screenshots/           # Visual snapshots of key outputs and notebooks
│
├── src/                   # Reusable Python modules to keep notebooks clean
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── visualization.py
│
├── requirements.txt       # Environment dependencies
└── README.md              # Project documentation
```

---

## 🛠️ Tech Stack & Tools
* **Language:** Python 3.x
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Environment:** Jupyter Notebook, VS Code

---

## 🔍 Analytical Pipeline Methodology
* **Data Understanding:** Loaded the raw dataset (`ecommerce_orders_raw.csv`) to audit structural integrity, identify missing values, and locate duplicate rows.
* **Data Cleaning:** Handled null values via relational lookup and statistical imputation, stripped duplicates, standardized text casing and date formats, and exported a single source of truth (`ecommerce_orders_cleaned.csv`) to `data/processed/`.
* **Univariate Analysis:** Analyzed individual variable distributions (`Total_Sales`, `Unit_Price`, `Customer_Age`, `Category`) and isolated extreme outliers using histograms and boxplots.
* **Bivariate Analysis:** Examined feature interactions using scatter plots and categorical aggregations to identify linear relationships and revenue drivers across regions and segments.
* **Multivariate Analysis:** Generated a correlation matrix across numerical features to evaluate multicollinearity and feature dependencies.
* **Final EDA & Feature Engineering:** Synthesized findings, validated `Total_Sales` calculations, and aggregated high-level business metrics.

---

## 📊 Key Findings & Reports
Detailed analytical conclusions and data quality logs can be found in the `reports/` directory:
* 📄 **[Data Quality Report](reports/data_quality_report.md):** Null-handling, deduplication, and anomaly resolution logs.
* 📈 **[Analytical Findings](reports/analytical_findings.md):** Univariate, bivariate, and multivariate statistical insights.
* 📋 **[Final Summary](reports/final_summary.md):** Executive business summary and actionable recommendations.

---

## 👤 Author
**Aziz Chharchhodawala**  
Data Analytics Intern at CodeAlpha  
[![LinkedIn](https://shields.io)](hwww.linkedin.com/in/aziz-chharchhodawala)
