from django.urls import re_path
from crypto import consumers
from bourse import brs_consumers, fav_namad_brs_consumers
from home import homeBS_consumers, homeCP_consumers

websocket_urlpatterns = [
    re_path(r'home/bourse/ws/$', homeBS_consumers.WatchConsumers.as_asgi()),
    re_path(r'home/crypto/ws/$', homeCP_consumers.WatchConsumers.as_asgi()),
    re_path(r'crypto/ws/$', consumers.WatchConsumers.as_asgi()),
    re_path(r'market-bourse/ws/$', brs_consumers.WatchConsumers.as_asgi()),
    re_path(r'fav-named-bourse/ws/$', fav_namad_brs_consumers.WatchConsumers.as_asgi()),
]
