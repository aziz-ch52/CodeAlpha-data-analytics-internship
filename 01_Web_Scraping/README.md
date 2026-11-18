# 🕸️ Task 01: Web Scraping – Books to Scrape Catalog Pipeline

> Automated, modular, and unit-tested Python web scraping pipeline built to extract, clean, validate, and export structured book catalog data from [Books to Scrape](https://books.toscrape.com/) as part of the **CodeAlpha Data Analytics Internship (November – December 2026)**.

---

## 📌 Project Overview

Web scraping is the foundational step in real-world data analytics workflows where structured datasets are not readily available via APIs or flat files.

This project implements a clean, production-style data extraction pipeline targeting **Books to Scrape** (`https://books.toscrape.com/`), a dedicated e-commerce sandbox containing **1,000 books across 50 paginated catalog pages**. Rather than relying on fragile monolithic scripts, the codebase separates HTTP session management, HTML parsing, data cleaning, data export, and automated testing into dedicated Python modules.

---

## 🎯 Objectives

- Inspect and navigate multi-page HTML DOM structures programmatically.
- Build a resilient HTTP client with retry strategies, custom User-Agent headers, and polite rate limiting.
- Extract key product attributes (title, price, star rating, stock availability, product URL, cover image URL).
- Clean and standardize raw extracted data (resolving currency encoding artifacts and mapping ordinal text ratings to numeric integers).
- Export both untouched raw snapshots and analysis-ready datasets in `CSV` and `JSON` formats.
- Validate parser accuracy and edge-case handling using automated `pytest` unit tests.

---

## 🗂️ Folder Structure

```text
01_Web_Scraping/
│
├── data/
│   ├── raw/                        # Untouched scraped snapshots (books_raw.csv, books_raw.json)
│   ├── processed/                  # Cleaned, typed, deduplicated datasets (books_cleaned.csv, books_cleaned.json)
│   └── README.md                   # Data directory documentation
│
├── notebooks/
│   └── 01_web_scraping.ipynb       # Interactive Jupyter Notebook for step-by-step execution & auditing
│
├── reports/
│   └── scraping_summary.md         # Execution summary, schema documentation, and data quality audit
│
├── screenshots/                    # Terminal, notebook, and output verification screenshots
│
├── src/
│   ├── __init__.py                 # Package initializer exposing core pipeline components
│   ├── scraper.py                  # Pagination crawler, session retry logic, and pipeline orchestrator
│   ├── parser.py                   # BeautifulSoup (lxml) HTML element extraction & URL resolution
│   ├── data_cleaning.py            # Price normalization, rating mapping, type casting, and deduplication
│   └── data_export.py              # Automated directory creation and CSV/JSON serialization
│
├── tests/
│   └── test_parser.py              # Unit tests for HTML parsing, pagination links, and price cleaning
│
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation