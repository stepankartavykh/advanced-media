"""Module to work with one page. Parse and make some necessary operations to analyse the content of the page."""

import requests
from bs4 import BeautifulSoup
import configparser


config_parser = configparser.ConfigParser()
config_parser.read('/home/skartavykh/PycharmProjects/advanced-media/development.ini')


class PageHandler:
    """Class to build page object to process coming page."""
    def __init__(self, page_url):
        """Initialize page. Get page source HTML code."""
        self.url = page_url
        self.content = requests.get(page_url).content.decode('utf-8')

    def generate_file_name(self, file_name):
        storage_dir = config_parser['DEFAULT']['STORAGE_PATH']
        return storage_dir + f'/{file_name}'

    def write_page_source_code_to_file(self, path_to_file: str = None):
        path = 'STORAGE_PATH'
        if path_to_file:
            path = path_to_file
        path = path + '.html'
        with open(path, 'w') as file_page:
            file_page.write(self.content)

    def get_all_links_from_page(self):
        """Get all available links on page. For next iteration of search."""
        page = str(BeautifulSoup(self.content, features="html.parser"))

        while True:
            start_link = page.find("a href")
            if start_link == -1:
                return None, 0
            start_quote = page.find('"', start_link)
            end_quote = page.find('"', start_quote + 1)
            founded_url = page[start_quote + 1: end_quote]

            page = page[end_quote:]
            if founded_url:
                print(founded_url)
            else:
                break


if __name__ == '__main__':
    url_ = 'https://google.com'
    google_handler = PageHandler(url=url_)
    google_handler.write_page_source_code_to_file()
