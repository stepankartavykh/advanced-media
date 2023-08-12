"""Module to work with one page. Parse and make some necessary operations to analyse the content of the page."""
import requests

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


if __name__ == '__main__':
    url_ = 'https://google.com'
    google_handler = PageHandler(url=url_)
    google_handler.write_page_source_code_to_file()
