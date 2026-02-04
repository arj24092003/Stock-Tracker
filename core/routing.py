from django.urls import re_path
from core.consumers import LiveStockConsumer

websocket_urlpatterns = [
    re_path(r"ws/stocks/?$", LiveStockConsumer.as_asgi()),
]


