from time import sleep
import requests
from bs4 import BeautifulSoup

content = None
data_list = []


class ScrapExceptions(Exception):
    pass


def send_request():
    global content
    url = 'https://www.sena.ir/'
    try:
        response = requests.get(url)
        content = BeautifulSoup(response.text, 'html.parser')

    except ScrapExceptions:
        sleep(30)
        send_request()


def get_news_data(*args):
    for id in args:
        get_titles = content.select(f'section#{id} li h3 a')
        get_imgs = content.select(f'section#{id} li img') or 'not found'
        get_urls = content.select(f'section#{id} li figure a')
        for index in range(0, len(get_titles)):
            datas_info = {
                f'{id}_{index}': {
                    'title': get_titles[index].text or "null",
                    'img': get_imgs[index].get('src') or "null",
                    'url': get_urls[index].get('href') or "null",
                }
            }
            data_list.append(datas_info)

