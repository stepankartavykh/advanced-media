"""Module to work with one page. Parse and make some necessary operations to analyse the content of the page."""
import requests
from bs4 import BeautifulSoup
from config import STORAGE_PATH


class PageHandler:
    """Class to build page object to process coming page."""
    def __init__(self, url):
        """Initialize page. Get page source HTML code."""
        self.url = url
        self.content = requests.get(url).content.decode('utf-8')

    def write_page_source_code_to_file(self, path_to_file: str = None):
        path = STORAGE_PATH
        path = path_to_file if path_to_file else STORAGE_PATH
        path = path + '.html'
        with open(path, 'w') as file_page:
            file_page.write(self.content)

    def get_all_links_from_page(self) -> list[str]:
        """Get all available links on page. For next iteration of search."""
        page = str(BeautifulSoup(self.content))

        def get_url(page):
            """

            :param page: html of web page (here: Python home page)
            :return: urls in that page
            """
            start_link = page.find("a href")
            if start_link == -1:
                return None, 0
            start_quote = page.find('"', start_link)
            end_quote = page.find('"', start_quote + 1)
            url = page[start_quote + 1: end_quote]
            return url, end_quote

        while True:
            url, n = get_url(page)
            page = page[n:]
            if url:
                print(url)
            else:
                break


if __name__ == '__main__':
    url_ = 'https://google.com'
    google_handler = PageHandler(url=url_)
    google_handler.write_page_source_code_to_file()
