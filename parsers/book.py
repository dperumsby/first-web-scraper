import logging

from locators.books_locators import BooksLocators


logger = logging.getLogger('scraping.book_parser')


class BookParser:
    def __init__(self, parent):
        logger.debug('New book parser created from HTML parent')
        self.parent = parent

    def __repr__(self):
        if self.rating == 1:
            return f'<"{self.title}" has {self.rating} star and costs £{self.price}>'
        else:
            return f'<"{self.title}" has {self.rating} stars and costs £{self.price}>'

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    @property
    def title(self):
        logger.debug('Finding book name...')
        locator = BooksLocators.TITLE
        title = self.parent.select_one(locator).attrs['title']
        logger.info(f'Found book name, `{title}`')
        return title

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BooksLocators.RATING
        number = self.parent.select_one(locator).attrs['class'][1]
        rating = BookParser.RATINGS[number]
        logger.info(f'Found book rating, `{rating}`')
        return rating

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BooksLocators.PRICE
        price = self.parent.select_one(locator).string
        price_formatted = '{:.2f}'.format(float(price[1:]))
        logger.info(f'Found price, `{price_formatted}`')
        return price_formatted
        


        