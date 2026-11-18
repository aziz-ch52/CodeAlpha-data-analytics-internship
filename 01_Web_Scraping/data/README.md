# 📂 Data Directory

This folder stores the raw and processed datasets extracted from **[Books to Scrape](https://books.toscrape.com/)**.

## 🔄 How the Data Was Collected

1. **Source:** Crawled all **50 catalog pages** (`https://books.toscrape.com/catalogue/page-1.html` to `page-50.html`) using `src/scraper.py` (`requests` + `BeautifulSoup4`).
2. **Raw Extraction (`raw/`):** Saved the untouched scraped records (`books_raw.csv` & `books_raw.json`) immediately after HTML parsing.
3. **Cleaning & Export (`processed/`):** Processed the raw records via `src/data_cleaning.py` and `src/data_export.py`—stripping currency encoding artifacts (`Â£`), converting text ratings (`One`–`Five`) to integers, adding boolean stock flags, and deduplicating URLs—to produce `books_cleaned.csv` and `books_cleaned.json` (**1,000 books** total).

## 🗂️ Contents

- **`raw/`**: `books_raw.csv`, `books_raw.json` — Original scraped output before preprocessing.
- **`processed/`**: `books_cleaned.csv`, `books_cleaned.json` — Analysis-ready datasets used for downstream EDA and visualization.

> **Regenerate Data:** Run `python -m src.scraper` from the `01_Web_Scraping/` directory to re-fetch and rebuild all files automatically.