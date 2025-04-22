import pytest

import library
from book import Book


def test_add_book():
    library_1 = library.Library()
    b = Book("rrr", "bbb")
    b2 = Book('rr', '44')
    b3 = Book('1233by', '44$🤣')
    library_1.add_book(b)
    library_1.add_book(b2)
    library_1.add_book(b3)
    assert b in library_1.books
    assert b2 in library_1.books
    assert b3 in library_1.books


def test_add_user():
    library_1 = library.Library()
    u = ('', '')
    library_1.add_user(u)
    assert u in library_1.users
