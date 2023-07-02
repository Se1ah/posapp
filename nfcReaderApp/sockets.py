from nfc.clf import ContactlessFrontend
import json
from nfc.clf import RemoteTarget

from channels.generic.websocket import WebsocketConsumer

class NFCConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        #self.send(json.dumps({'tag': "data"}))
    
    def receive(self, text_data=None, bytes_data=None):
        print("receive")
        clf = ContactlessFrontend('usb')  # Use the appropriate transport for your NFC reader
        target = clf.sense(RemoteTarget('106A'))
        if target is not None:
            self.send(json.dumps({'tag': str(target)}))

    def disconnect(self, close_code):
        pass
