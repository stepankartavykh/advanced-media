import requests


sites = [
    "https://www.rbc.ru/",
    "https://www.kommersant.ru/"
    "https://lenta.ru/",
]


def get_data_sites():
    output = []
    for site in sites:
        data_site = requests.get(url=site).json()
        output.append(data_site)
    return requests.get(url="https://www.rbc.ru/").content.decode('utf-8')
