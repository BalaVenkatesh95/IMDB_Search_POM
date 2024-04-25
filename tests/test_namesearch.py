# tests/test_namesearch.py
from pages.name_search_page import NameSearchPage


url = "https://www.imdb.com/search/name/"

search_page = NameSearchPage(url)

def test_name_search():
    search_page.name_search()

def test_shutdown():
    search_page.shutdown()

