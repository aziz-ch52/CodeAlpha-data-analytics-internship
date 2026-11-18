from typing import Dict, List
from urllib.parse import urljoin
from bs4 import BeautifulSoup

RATING_MAP: Dict[str, int] = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
}


def parse_books_from_html(html: str, page_url: str) -> List[Dict]:
    """Extract book metadata from a single catalog page HTML."""
    soup = BeautifulSoup(html, "lxml")
    articles = soup.select("article.product_pod")
    records: List[Dict] = []

    for article in articles:
        title_tag = article.select_one("h3 a")
        price_tag = article.select_one("p.price_color")
        availability_tag = article.select_one("p.instock.availability")
        rating_tag = article.select_one("p.star-rating")
        img_tag = article.select_one("div.image_container img")

        title = title_tag["title"].strip() if title_tag and title_tag.has_attr("title") else ""
        relative_href = title_tag["href"] if title_tag and title_tag.has_attr("href") else ""
        product_url = urljoin(page_url, relative_href)

        raw_price = price_tag.get_text(strip=True) if price_tag else ""
        availability = availability_tag.get_text(strip=True) if availability_tag else ""

        rating_word = ""
        if rating_tag and rating_tag.has_attr("class"):
            classes = [c for c in rating_tag["class"] if c != "star-rating"]
            rating_word = classes[0] if classes else ""

        relative_img = img_tag["src"] if img_tag and img_tag.has_attr("src") else ""
        image_url = urljoin(page_url, relative_img)

        records.append(
            {
                "title": title,
                "raw_price": raw_price,
                "rating_text": rating_word,
                "rating": RATING_MAP.get(rating_word, 0),
                "availability": availability,
                "product_url": product_url,
                "image_url": image_url,
            }
        )

    return records


def get_next_page_url(html: str, current_url: str) -> str | None:
    """Return the absolute URL for the next pagination page, or None if on the last page."""
    soup = BeautifulSoup(html, "lxml")
    next_link = soup.select_one("li.next a")
    if next_link and next_link.has_attr("href"):
        return urljoin(current_url, next_link["href"])
    return None