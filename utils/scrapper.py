import os
import time
import requests


url = "https://www.rbc.ru/"


def get_html_page(_url: str) -> str:
    content = requests.get(_url).content.decode('utf-8')
    return content


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


if __name__ == '__main__':
    get_info("first_launch", 2)
