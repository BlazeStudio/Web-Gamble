# example/views.py
import math
import random
from datetime import datetime


from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import messages

def index(request):
    return render(request, 'home.html')

def high_low(request, value = 0):
    return render(request, 'high_low.html', {'value': value})

def bet(request):
    action = request.GET.get('action')
    ratio = int(request.GET.get('ratio'))
    max_value = round(999999 * (ratio/100))
    min_value = round((999999 * (1 - ratio / 100)))
    value = random.randint(0, 999999)
    if ((action == 'higher') and (value >= min_value)) or ((action == 'lower') and (value <= max_value)):
        message = "Winner!"
        # messages.success(request, "Winner!")
    else:
        message = "Loser!"
        # messages.error(request, "Loser!")
    return JsonResponse({'value': value, 'message': message})