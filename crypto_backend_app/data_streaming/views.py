from django.shortcuts import render
from coins.models import Coin


# Create your views here.

def main(request):
    coins = Coin.objects.all()
    return render(request, 'data_streaming/main.html', {'coins': coins})


def dashboard(request, slug):
    return render(request, 'data_streaming/dashboard.html', {})
