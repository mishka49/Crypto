# import json

import requests

# from coins import serializers
# from coins.models import Coin
# from coins.repositories import CoinRepository
# from coins.serializers import CoinSerializer


# class UpdaterService:
#     @staticmethod
#     def update_coins(coins):
#         print(f"Coins: {coins}")
#         for coin in coins:
#             serializer = CoinSerializer(data=coin)
#             if serializer.is_valid():
#                 print("API valided")
#                 continue
#
#             print("API None")
#             CoinRepository.create_or_update(coin)
#
#
# class ExternalApiHandler:
#     @staticmethod
#     def get_coins():
#         request = requests.get('https://api.coinlore.net/api/tickers/')
#
#         for coin in request.json()['data']:
#             print(coin)
#             serializer = CoinSerializer(data=coin)
#
#             for field in Coin._meta.fields:
#                 print('model', 'request')
#                 print(field.value, coin[field.name])
#
#             if not serializer.is_valid():
#                 print("API NONE")
#                 return None
#
#         return request.json()

    # @staticmethod
    # def get_coin():
    #     pass


def get_info():
    import json
    import websocket
    import pandas as pd

    assets = ['BTCUSDT']

    assets = [coin.lower() + '@kline_1m' for coin in assets]
    assets = '/'.join(assets)

    def on_message(mw, message):
        message = json.loads(message)
        print(message)

    socket = "wss://stream.binance.com:9443/stream?streams=" + assets

    ws = websocket.WebSocketApp(socket, on_message=on_message)

    ws.run_forever()


class APIService:
    pass


class CoinsUpdater:
    pass


class UpdaterFacadeService:
    def __init__(self, update_frequency, coins_list, api_service=APIService(), updater=CoinsUpdater):
        self.update_frequency = update_frequency
        self.coins_list = coins_list
        self.api_service = api_service
        self.updater = updater

    def run_stream(self):
        pass

    def stop_stream(self):
        pass



if __name__ == '__main__':
    # coins = ExternalApiHandler.get_coins()
    # UpdaterService.update_coins(coins)

    get_info()
