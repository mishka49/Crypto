# import json
import asyncio
import json
import threading
import time

import requests

from coins.models import Coin
from coins.repositories import CoinRepository


class UpdaterService:
    @staticmethod
    def update_coins(coins):
        print(f"Coins: {coins}")
        for coin in coins['data']:
            coin = Coin(
                id = coin['id'],
                symbol=coin['symbol'],
                name=coin['name'],
                rank=coin['rank'],
                price_usd=coin['price_usd'],
                percent_change_24h=coin['percent_change_24h'],
                percent_change_1h=coin['percent_change_1h'],
                percent_change_7d=coin['percent_change_7d'],
                market_cap_usd=coin['market_cap_usd']
            )

            print("API None")
            CoinRepository.create_or_update(coin)


class ExternalApiHandler:
    @staticmethod
    def get_coins():
        request = requests.get('https://api.coinlore.net/api/tickers/')
        return request.json()

    # @staticmethod
    # def get_price_coin(coin_id: str, last_days: int):
    #     import requests
    #     import pandas as pd
    #     import matplotlib.pyplot as plt
    #
    #     # Define the cryptocurrency symbol (e.g., BTC for Bitcoin)
    #     crypto_symbol = "BTC"
    #
    #     # Define the API endpoint for historical data
    #     url = f"https://api.coingecko.com/api/v3/coins/{crypto_symbol.lower()}/market_chart"
    #
    #     # Set the date range (last month)
    #     end_date = pd.Timestamp.now()
    #     start_date = end_date - pd.DateOffset(months=1)
    #
    #     # Convert dates to Unix timestamps
    #     start_timestamp = int(start_date.timestamp())
    #     end_timestamp = int(end_date.timestamp())
    #
    #     # Define the parameters for the API request
    #     params = {
    #         "vs_currency": "USD",
    #         "from": start_timestamp,
    #         "to": end_timestamp,
    #         "days": 30,
    #     }
    #
    #     # Make the API request
    #     response = requests.get(url, params=params)
    #     data = response.json()
    #     print(data)
    #     # Extract timestamps and prices
    #     timestamps = [pd.Timestamp.fromtimestamp(ts / 1000) for ts in data["prices"]]
    #     prices = [price[1] for price in data["prices"]]
    #
    #     # Create a DataFrame
    #     df = pd.DataFrame({"Timestamp": timestamps, "Price (USD)": prices})
    #
    #     # Plot the price data
    #     plt.figure(figsize=(10, 6))
    #     plt.plot(df["Timestamp"], df["Price (USD)"], marker="o", linestyle="-", color="b")
    #     plt.title(f"{crypto_symbol} Price (Last Month)")
    #     plt.xlabel("Date")
    #     plt.ylabel("Price (USD)")
    #     plt.grid(True)
    #     plt.show()


import websocket


class CoinDataStreamer(threading.Thread):
    SOCKET_URL = "wss://stream.binance.com:9443/stream?streams="

    def __init__(self, coin_name: str, handler=lambda mw, message: print(message)):
        threading.Thread.__init__(self)
        self.coin_name = coin_name
        self.websocket = self.create_websocket(handler)

    def create_websocket(self, handler):
        asset = self.coin_name.lower() + '@kline_1m'
        ws = self.SOCKET_URL + asset
        return websocket.WebSocketApp(ws, on_message=handler)

    def run(self):
        self.websocket.run_forever()

    def stop_websocket(self):
        self.websocket.close()


if __name__ == '__main__':
    # coins = ExternalApiHandler.get_coins()
    # print(coins)
    # UpdaterService.update_coins(coins)

    # socket = CoinDataStreamer('BTCUSDT', lambda mw, message: print(json.loads(message)['data']['k']['c']))
    # socket.start()
    # time.sleep(10)
    # socket.stop_websocket()

    ExternalApiHandler.get_price_coin('fghj', 12)

    # get_info()
