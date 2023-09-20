import os
import time
import requests

from utils import PageHandler


url = "https://www.rbc.ru/"


def get_html_page(_url: str) -> str:
    content = requests.get(_url).content.decode('utf-8')
    return content


def get_all_links_from_page(html_code: str):
    pass


def get_info(launch_code: str, time_between_requests: int) -> None:
    dir_path = f"pages_launch_{launch_code}"
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    i = 0
    while True:
        page_str = get_html_page(url)
        print(len(page_str))
        with open(f'{dir_path}/page{i}.html', 'w') as file_page:
            file_page.write(page_str)
        time.sleep(time_between_requests)
        i += 1


def start(start_url):
    added_links = set()

    def run_process(incoming_url: str):
        handler = PageHandler(incoming_url)
        handler.get_all_links_from_page()
        for link in handler.links:
            if link not in added_links:
                added_links.add(link)
                print(link)
                run_process(link)
            # internal_handler = PageHandler(link)
            # internal_handler.get_all_links_from_page()

    run_process(start_url)


if __name__ == '__main__':
    # get_info("third_launch", 2)
    start("https://www.google.ru/")
