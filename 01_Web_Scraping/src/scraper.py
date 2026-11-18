import logging
import time
from typing import Dict, List
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .parser import parse_books_from_html, get_next_page_url
from .data_cleaning import clean_books_data
from .data_export import export_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)


class BookScraper:
    """Scraper for crawling all catalog pages on books.toscrape.com."""

    def __init__(
        self,
        start_url: str = "https://books.toscrape.com/catalogue/page-1.html",
        delay: float = 0.25,
    ) -> None:
        self.start_url = start_url
        self.delay = delay
        self.session = self._build_session()

    @staticmethod
    def _build_session() -> requests.Session:
        session = requests.Session()
        session.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/128.0.0.0 Safari/537.36"
                )
            }
        )
        retries = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retries)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def fetch_html(self, url: str) -> str:
        response = self.session.get(url, timeout=15)
        response.raise_for_status()
        response.encoding = "utf-8"
        return response.text

    def scrape_all(self, max_pages: int | None = None) -> List[Dict]:
        all_books: List[Dict] = []
        current_url: str | None = self.start_url
        page_count = 0

        while current_url:
            if max_pages is not None and page_count >= max_pages:
                break

            page_count += 1
            logger.info("Scraping page %d: %s", page_count, current_url)
            html = self.fetch_html(current_url)

            page_books = parse_books_from_html(html, current_url)
            all_books.extend(page_books)

            current_url = get_next_page_url(html, current_url)
            if current_url:
                time.sleep(self.delay)

        logger.info("Finished scraping %d books across %d pages.", len(all_books), page_count)
        return all_books


def main() -> None:
    scraper = BookScraper()
    raw_books = scraper.scrape_all()
    cleaned_df = clean_books_data(raw_books)
    export_data(raw_books, cleaned_df)
    logger.info("Data exported successfully to data/raw and data/processed.")


if __name__ == "__main__":
    main()