from django.shortcuts import render
import requests


def home(request):
    # Grab Crypto Price Data
    prices = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD").json()

    # Grab Crypto News Data
    newses = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN").json()

    context = {
        'prices': prices['DISPLAY'],
        'newses': newses['Data'],
    }

    return render(request, 'crypto/home.html', context)


def prices(request):
    notfound = False
    if request.method == 'POST':
        quote = request.POST.get('quote').upper()
        prices = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=USD").json()
        return render(request, 'crypto/prices.html', {'quote': quote, 'prices': prices})
    else:
        notfound = True
    return render(request, 'crypto/prices.html', {'notfound': notfound})
