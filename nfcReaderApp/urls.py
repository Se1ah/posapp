from django.urls import re_path

from nfcReaderApp.sockets import NFCConsumer


urlpatterns = []

websocket_urlpatterns = [
    re_path('nfc/', NFCConsumer.as_asgi()),
]
