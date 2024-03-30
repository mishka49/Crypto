import json

from channels.generic.websocket import AsyncWebsocketConsumer


class DashBoardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connection')
        await self.accept()

    async def disconnect(self, close_code):
        print(f'connection closed with code: {close_code}')

    async def receive(self, text_data):
        test_data_json = json.loads(text_data)
        message = test_data_json["message"]
        sender = test_data_json["sender"]

        print(message, sender)

        await self.send(text_data=json.dumps(
            {
                'message': message,
                'sender': sender,
            }
        ))
