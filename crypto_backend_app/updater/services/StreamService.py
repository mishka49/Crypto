from updater.services.api_service import APIService

from updater.services.coin_updater_service import CoinsUpdater


class StreamService:
    def __init__(self, update_frequency, coins_list, api_service=APIService(), updater=CoinsUpdater):
        self.update_frequency = update_frequency
        self.coins_list = coins_list
        self.api_service = api_service
        self.updater = updater

    def run_stream(self):
        pass

    def stop_stream(self):
        pass
