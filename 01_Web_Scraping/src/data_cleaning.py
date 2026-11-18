import re
from typing import Dict, List
import pandas as pd


def clean_price(raw_price: str) -> float:
    """Strip currency symbols and encoding artifacts (e.g., 'Â£51.77' -> 51.77)."""
    if not raw_price:
        return 0.0
    cleaned = re.sub(r"[^\d.]", "", str(raw_price))
    return float(cleaned) if cleaned else 0.0


def clean_books_data(raw_records: List[Dict]) -> pd.DataFrame:
    """Convert raw scraped records into a clean, typed, deduplicated DataFrame."""
    df = pd.DataFrame(raw_records)
    if df.empty:
        return df

    df["title"] = df["title"].astype(str).str.strip()
    df["price_gbp"] = df["raw_price"].apply(clean_price)
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce").fillna(0).astype(int)
    df["availability"] = df["availability"].astype(str).str.strip()
    df["in_stock"] = df["availability"].str.lower().str.contains("in stock")

    # Drop duplicates based on unique product URL
    df = df.drop_duplicates(subset=["product_url"]).reset_index(drop=True)

    # Reorder columns for downstream analysis
    columns = [
        "title",
        "price_gbp",
        "rating",
        "availability",
        "in_stock",
        "product_url",
        "image_url",
    ]
    return df[columns]