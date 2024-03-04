import json

import requests


class Updater:
    @staticmethod
    def update_coins():
        print("start update")


class ExternalApiHandler:
    @staticmethod
    def get_coins():
        request = requests.get('https://api.coinlore.net/api/tickers/')
        print(json.loads(request.text)['data'])

    @staticmethod
    def get_coin():
        pass


if __name__ == '__main__':
    ExternalApiHandler.get_coins()
