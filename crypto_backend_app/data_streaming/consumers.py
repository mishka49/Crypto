from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

import websocket
from updater.services import CoinDataStreamer


class DashboardConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.coin_data_streamer = CoinDataStreamer('BTCUSDT', handler=self._handler)
        self.coin_data_streamer.start()

    def _handler(self, mw, message):
        self.send(text_data=json.dumps({'message': message}))

    def disconnect(self, close_code):
        self.coin_data_streamer.stop_websocket()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))
