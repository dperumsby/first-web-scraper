import requests
import logging

from pages.books_pages import BooksPage


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')

logger.info('Loading books list...')

page_content = requests.get(f"http://books.toscrape.com").content
page = BooksPage(page_content)
books = page.books
page_count = page.page_count 

for i in range(1, page_count + 1):
    url = f"http://books.toscrape.com/catalogue/page-{i}.html"
    page_content = requests.get(url).content
    logger.debug('Creating BooksPage from page content')
    page = BooksPage(page_content)
    books.extend(page.books)
