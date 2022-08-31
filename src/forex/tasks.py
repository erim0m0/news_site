from celery import shared_task
from forex.models import ForexData
from . import forex_scrap


@shared_task
def add_forex_price():
    forex_scrap.get_data()
    data_list = forex_scrap.data_list
    ForexData.objects.all().delete()
    ForexData.objects.bulk_create(
        [ForexData(**{
            'price_name': num,
            'price': data_list[num - 1]
        }) for num in range(1,3)])
    return
