from src.parser import parse_books_from_html, get_next_page_url
from src.data_cleaning import clean_price, clean_books_data

SAMPLE_HTML = """
<html>
  <body>
    <article class="product_pod">
      <div class="image_container">
        <a href="a-light-in-the-attic_1000/index.html">
          <img src="../media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" />
        </a>
      </div>
      <p class="star-rating Three"></p>
      <h3>
        <a href="a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a>
      </h3>
      <div class="product_price">
        <p class="price_color">Â£51.77</p>
        <p class="instock availability">In stock</p>
      </div>
    </article>
    <ul class="pager">
      <li class="next"><a href="page-2.html">next</a></li>
    </ul>
  </body>
</html>
"""


def test_parse_books_from_html():
    base_url = "https://books.toscrape.com/catalogue/page-1.html"
    books = parse_books_from_html(SAMPLE_HTML, base_url)

    assert len(books) == 1
    assert books[0]["title"] == "A Light in the Attic"
    assert books[0]["rating"] == 3
    assert books[0]["availability"] == "In stock"
    assert books[0]["product_url"] == "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"


def test_get_next_page_url():
    base_url = "https://books.toscrape.com/catalogue/page-1.html"
    next_url = get_next_page_url(SAMPLE_HTML, base_url)
    assert next_url == "https://books.toscrape.com/catalogue/page-2.html"


def test_clean_price_handles_encoding_artifacts():
    assert clean_price("Â£51.77") == 51.77
    assert clean_price("£12.50") == 12.50
    assert clean_price("") == 0.0


def test_clean_books_data_pipeline():
    base_url = "https://books.toscrape.com/catalogue/page-1.html"
    raw = parse_books_from_html(SAMPLE_HTML, base_url)
    df = clean_books_data(raw)

    assert len(df) == 1
    assert df.loc[0, "price_gbp"] == 51.77
    assert bool(df.loc[0, "in_stock"]) is True