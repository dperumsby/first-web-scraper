import logging

from app import books


logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''Please choose one of the following:

- 'b' to look at the top five books
- 'c' to look at the cheapest five books
- 'n' to look at the next book
- 'q' to exit

Please enter your choice: '''


def print_top_five_books():
    logger.info('Getting top five books by rating...')
    sorted_books = sorted(books, key=lambda x: x.rating, reverse=True)
    for book in sorted_books[:5]:
        print(book)


def print_cheapest_five_books():
    logger.info('Getting top five books by cheapest price...')
    sorted_books = sorted(books, key=lambda x: x.price)
    for book in sorted_books[:5]:
        print(book)


books_generator = (book for book in books)


def print_next_book():
    logger.info('Printing next book from generator...')
    print(next(books_generator))


user_choice = {
    'b': print_top_five_books,
    'c': print_cheapest_five_books,
    'n': print_next_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in {'b', 'c', 'n'}:
            user_choice[user_input]()
        else:
            print('Please enter a valid option')
        user_input = input(USER_CHOICE)
    logger.debug('Terminating program...')


menu()
