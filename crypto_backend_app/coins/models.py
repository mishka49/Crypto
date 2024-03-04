from django.db import models


class Coin(models.Model):
    symbol = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    rank = models.IntegerField()
    price_usd = models.CharField(max_length=20)
    percent_change_24h = models.FloatField()
    percent_change_1h = models.FloatField()
    percent_change_7d = models.FloatField()
    market_cap_usd = models.CharField(max_length=40)

class CoinData(models.Model):
    coin = models.ForeignKey('Coin', on_delete=models.CASCADE)
    price_usd = models.CharField(max_length=20)
    datetime = models.DateTimeField()
