import json

import requests

from coins import serializers
from coins.models import Coin
from coins.repositories import CoinRepository
from coins.serializers import CoinSerializer


class UpdaterService:
    @staticmethod
    def update_coins(coins):
        print(f"Coins: {coins}")
        for coin in coins:
            serializer = CoinSerializer(data=coin)
            if serializer.is_valid():
                print("API valided")
                continue

            print("API None")
            CoinRepository.create_or_update(coin)


class ExternalApiHandler:
    @staticmethod
    def get_coins():
        request = requests.get('https://api.coinlore.net/api/tickers/')

        for coin in request.json()['data']:
            print(coin)
            serializer = CoinSerializer(data=coin)

            for field in Coin._meta.fields:
                print('model', 'request')
                print(field.value, coin[field.name])

            if not serializer.is_valid():
                print("API NONE")
                return None
 
        return request.json()




    @staticmethod
    def get_coin():
        pass


if __name__ == '__main__':
    coins = ExternalApiHandler.get_coins()
    UpdaterService.update_coins(coins)
