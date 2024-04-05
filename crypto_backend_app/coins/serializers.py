from rest_framework import serializers

from coins.models import Coin


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin,
        fields = ['id', 'symbol', 'name', 'rank', 'price_usd', 'percent_change_24h', 'percent_change_1h',
                  'percent_change_7d', 'market_cap_usd']
