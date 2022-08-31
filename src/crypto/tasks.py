from celery import shared_task
from crypto.models import CrptDataNews
from crypto import scrap_crypto


@shared_task
def add_crypto_news():
    scrap_crypto.send_request()
    scrap_crypto.get_news_data()
    data_list = scrap_crypto.data_list
    data = []
    for item in data_list:
        data.append(list(item.values()))
    CrptDataNews.objects.all().delete()
    CrptDataNews.objects.bulk_create(
        [CrptDataNews(**{
            'title_news': list(d[0].values())[0],
            'img_news': list(d[0].values())[1],
            'url_news': list(d[0].values())[2],
            'datetime': list(d[0].values())[3],
            'text': list(d[0].values())[4]
        }) for d in data])
    return

