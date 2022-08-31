from bs4 import BeautifulSoup
import requests
from time import sleep

content = None
data_list = []


class ScrapExceptions(Exception):
    pass


def send_request():
    global content
    url = 'https://www.coindesk.com/'
    try:
        response = requests.get(url, stream=True)
        content = BeautifulSoup(response.text, 'html.parser')

    except ScrapExceptions:
        sleep(25)
        send_request()


def get_news_data(*args):
    class_name = "containerstyles__StyledContainer-sc-292snj-0"
    get_data = content.select(f'div.{class_name} > section')[-1]
    class_name2 = "gridstyles__StyledGrid-eiwl28-0"
    get_data = get_data.select(f'div.{class_name2} > div')
    for index in range(4):
        source = get_data[index]
        img = source.find('source').get('srcset').split(',')[0][:-4]
        get_media = source.findChildren('div', recursive=False)
        url = get_media[0].find('a').get('href')
        title = get_media[1].find('a').text
        datetime = None
        get_text_and_datetime = get_media[1].findChildren('div', recursive=False)
        if len(get_text_and_datetime) == 2:
            text = get_text_and_datetime[0].text
            datetime = get_text_and_datetime[1].text
        else:
            text = "null"
            datetime = get_text_and_datetime[0].text
        datas_info = {
            f'{index + 1}': {
                'title': title or "null",
                'img': img or "null",
                'url': url or "null",
                'datetime': datetime or "null",
                'text': text or "null"
            }
        }

        data_list.append(datas_info)
send_request()
get_news_data()
for i in data_list:
    print(i)