from django.shortcuts import render
from .models import Coin
from updater.services import ExternalApiHandler, UpdaterService


def coins(request):
    ex_coins = ExternalApiHandler.get_coins()
    UpdaterService.update_coins(ex_coins)
    print("EXTERNAL", ex_coins)
    c = Coin.objects.order_by('-id')[:10]
    print("COINS", c)
    return render(request, 'coins/coins.html', context={'coins': c, 'col_index': 0})


def coins_filtered_by_name(request):
    c = Coin.objects.order_by('name')[:10]
    return render(request, 'coins/coins.html', context={'coins': c, 'col_index': 1})


def coins_filtered_by_rank(request):
    c = Coin.objects.order_by('rank')[:10]
    return render(request, 'coins/coins.html', context={'coins': c, 'col_index': 2})


def coins_filtered_by_price(request):
    c = Coin.objects.order_by('price_usd')[:10]
    return render(request, 'coins/coins.html', context={'coins': c, 'col_index': 3})


def coins_filtered_by_percent_change(request, segment):
    c = Coin.objects.order_by('name')
    col_index = 0

    match segment:
        case '7d':
            c = c.order_by('percent_change_7d')
            col_index = 5
        case '24h':
            c = c.order_by('percent_change_24h')
            col_index = 4
        case '1h':
            c = c.order_by('percent_change_1h')
            col_index = 6

    return render(request, 'coins/coins.html', context={'coins': c[:10], 'col_index': col_index})
