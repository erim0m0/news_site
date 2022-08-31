from celery import shared_task
from .models import BrsDataNews
from . import scrap_bourse


@shared_task
def add_notif():
    scrap_bourse.send_request()
    scrap_bourse.get_news_data(
        'carousel1', 'box173',
        'box172', 'box157'
    )
    data_list = scrap_bourse.data_list
    keys, values = [], []
    for data in data_list:
        for k, v in data.items():
            keys.append(k)
            values.append(v)
    BrsDataNews.objects.all().delete()
    BrsDataNews.objects.bulk_create(
        [BrsDataNews(**{
            'place_news': keys[data][:-2],
            'title_news': values[data]['title'],
            'img_news': values[data]['img'],
            'url_news': values[data]['url']
        }) for data in range(len(keys))])
    return
