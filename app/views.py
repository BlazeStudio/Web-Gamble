# example/views.py
import json
import math
import random
from datetime import datetime

from _decimal import Decimal, ROUND_HALF_UP
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages



def home(request):
    return render(request, 'home.html')

def games(request):
    with open("static/json/games.json", 'r', encoding="utf-8") as f:
        games_data = json.load(f)
    return render(request, 'games.html', {'games_data': games_data})


#DICE(HIGH/LOW)
def high_low(request):
    return render(request, 'high_low.html')


def bet(request):
    bet = (request.GET.get('bet'))
    message = {}
    if bet == "":return JsonResponse({'message': message})
    bet = Decimal(bet)
    balance = Decimal(request.GET.get('balance'))
    if balance < bet:
        message['type'] = 'error'
        message['text'] = 'Не хватает средств'
        return JsonResponse({'message': message})
    action = request.GET.get('action')
    ratio = Decimal(request.GET.get('ratio'))
    max_value = round(999999 * (ratio/100))
    min_value = round((999999 * (1 - ratio / 100)))
    value = random.randint(0, 999999)
    if ((action == 'higher') and (value >= min_value)) or ((action == 'lower') and (value <= max_value)):
        message['type'] = 'success'
        message['text'] = f'Поздравляем! Выпало {value}'
        win = (bet / (ratio / 100)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP) - bet
        print(win)
        balance += win
    else:
        message['type'] = 'error'
        message['text'] = f'Вы проиграли. Выпало {value}'
        balance -= bet
        # messages.error(request, "Loser!")
    return JsonResponse({'message': message, 'balance': balance})


#Mines
matrix = None
def mines(request):
    global matrix
    matrix = [['!' for _ in range(5)] for _ in range(5)]
    # Выбираем три случайных ячейки для заполнения крестиками
    #TODO - проверка на уникальность
    for _ in range(3):
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        matrix[row][col] = 'x'
        print('x', row, col)
    print(matrix)
    return render(request, 'mines.html', {'matrix': matrix})

def get_cell_content(request):
    global matrix
    row = int(request.GET.get('row'))
    col = int(request.GET.get('col'))
    content = matrix[row][col]
    # if (content == 'x'):
    #     return HttpResponseRedirect('/end_mines')
    return HttpResponse(content)

# def end_mines(request):
#     print("DEAD")
#     return HttpResponse("Dead")



