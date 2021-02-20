import re
import logging
from bs4 import BeautifulSoup

from locators.books_page_locators import BookPageLocators
from locators.books_locators import BooksLocators
from parsers.book import BookParser


logger = logging.getLogger('scraping.books_pages')


class BooksPage:
    def __init__(self, page):
        logger.debug('Parsing HTML with BeautifulSoup')
        self.soup = BeautifulSoup(page, 'html.parser') 

    @property
    def books(self):
        locator = BookPageLocators.BOOK
        book_tags = self.soup.select(locator)
        logger.debug(f'Finding all books in the page using `{locator}`')
        return [BookParser(e) for e in book_tags]

    @property
    def page_count(self):
        logger.debug('Finding number of pages in catalogue...')
        locator = BookPageLocators.PAGER
        pager = self.soup.select_one(locator).string.strip()
        pattern = r'\d+$'
        match = re.search(pattern, pager)
        pages = int(match.group(0))
        logger.info(f'Found number of pages in catalogue: `{pages}`')
        return pages



    