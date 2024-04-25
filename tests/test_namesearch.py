# tests/test_namesearch.py
import pytest
from ..pages.name_search_page import NameSearchPage
from ..utils.data_loader import load_json_data
from ..utils.screenshot import take_screenshot
from ..pages.base_page import BasePage

url = "https://www.imdb.com/search/name/"

imdb = BasePage(url)

def test_name_search(driver, artistname):
    search_page = NameSearchPage(driver)
    test_data = load_json_data("artistname_data.json", artistname)
    search_page.name_search(test_data["artistname"])
    take_screenshot(driver, "screenshots/search")
    take_screenshot(driver, "screenshots/login")

def test_shutdown():
    imdb.shutdown()

