import json
import websocket

class APIService:
    def __init__(self, coins_list):
        pass
    def get_current_coast(self):
        assets = ['BTCUSDT']

        assets = [coin.lower() + '@kline_1m' for coin in assets]
        assets = '/'.join(assets)

        def on_message(mw, message):
            message = json.loads(message)
            print(message)

        socket = "wss://stream.binance.com:9443/stream?streams=" + assets

        ws = websocket.WebSocketApp(socket, on_message=on_message)

        ws.run_forever()