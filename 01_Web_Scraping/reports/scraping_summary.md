# Web Scraping Execution Summary

## Target Overview
- **Target URL**: `https://books.toscrape.com/`
- **Total Pages Crawled**: 50
- **Total Records Extracted**: 1,000 books

## Extracted Schema

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `title` | `string` | Full title of the book |
| `price_gbp` | `float` | Cleaned book price in GBP (£) |
| `rating` | `int` | Star rating converted from text (`1` to `5`) |
| `availability` | `string` | Raw availability text (`In stock`) |
| `in_stock` | `bool` | Boolean availability flag |
| `product_url` | `string` | Direct URL to the book detail page |
| `image_url` | `string` | Direct URL to the cover thumbnail |

## Data Quality Notes
- **Encoding Fix**: Handled `Â£` UTF-8/Latin-1 encoding artifact during price parsing.
- **Missing Values**: 0 null records across all 1,000 catalog items.
- **Duplicates**: 0 duplicate product URLs detected.