from django.urls import re_path
from . import brs_consumers

websocket_urlpatterns = [
    re_path(r'brs/$', consumers.WatchConsumers.as_asgi()),
]
