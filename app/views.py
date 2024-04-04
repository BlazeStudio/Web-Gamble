# example/views.py
import json
import math
import random
from datetime import datetime

from _decimal import Decimal, ROUND_HALF_UP
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import messages


def index(request):
    return render(request, 'home.html')

def games(request):
    with open("static/json/games.json", 'r', encoding="utf-8") as f:
        games_data = json.load(f)
    return render(request, 'games.html', {'games_data': games_data})


#DICE(HIGH/LOW)
def high_low(request, value = 0):
    return render(request, 'high_low.html', {'value': value})


def bet(request):
    action = request.GET.get('action')
    ratio = Decimal(request.GET.get('ratio'))
    bet = Decimal(request.GET.get('bet'))
    print(bet)
    win = (bet * (1 - ratio / 100)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    print(1 - ratio / 100)
    max_value = round(999999 * (ratio/100))
    min_value = round((999999 * (1 - ratio / 100)))
    value = random.randint(0, 999999)
    message = {}
    if ((action == 'higher') and (value >= min_value)) or ((action == 'lower') and (value <= max_value)):
        message['type'] = 'success'
        message['text'] = 'Поздравляем! Вы выиграли!'
        # win = round((bet * (1 - ratio / 100)), 2)
        print("Вы выиграли - ", bet + win)
    else:
        message['type'] = 'error'
        message['text'] = 'Вы проиграли. Повезёт в следующий раз.'
        # messages.error(request, "Loser!")
    return JsonResponse({'value': value, 'message': message})