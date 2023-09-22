"""Module to work with one page. Parse and make some necessary operations to analyse the content of the page."""

import requests
from bs4 import BeautifulSoup
import configparser
from page_analyzer import Analyzer


config_parser = configparser.ConfigParser()
config_parser.read('/home/skartavykh/PycharmProjects/advanced-media/development.ini')


class StructuredPage:
    def __init__(self, content):
        self.content = content

    def form(self):
        struct = self.__parse_content()
        return struct

    def __parse_content(self):
        return {
            "page_url": "test_url",
            "info": "test_info",
        }


class PageHandler:
    """Class to build page object to process coming page."""
    def __init__(self, page_url):
        """Initialize page. Get page source HTML code."""
        self.url = page_url
        self.content = requests.get(page_url).text
        self.links = []
        self.structure = StructuredPage(self.content).form()

    def generate_file_path(self):
        storage_dir = config_parser['DEFAULT']['STORAGE_PATH']
        url_ = self.url.replace('/', '')
        return storage_dir + f'/{url_}'

    def write_page_source_code_to_file(self):
        path = self.generate_file_path()
        path = path + '.html'
        with open(path, 'w') as file_page:
            file_page.write(self.content)

    def get_all_links_from_page(self):
        """Get all available links on page. For next iteration of search."""
        soup = BeautifulSoup(self.content, features="html.parser")
        for link in soup.find_all('a'):
            link_str: str = link.get('href')
            if link_str and link_str != self.url and link_str.startswith('https://'):
                self.links.append(link.get('href'))

    def process_page_structure(self):
        analysis = Analyzer(self.structure)
        analysis.make_general_analysis()


if __name__ == '__main__':
    url = 'https://www.investing.com'
    google_handler = PageHandler(page_url=url)
    google_handler.write_page_source_code_to_file()
    google_handler.get_all_links_from_page()
    print(google_handler.links)
