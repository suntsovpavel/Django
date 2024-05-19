from django.shortcuts import render
from django.http import HttpResponse
import random
import logging
from .models import Game

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse('Hello World!')

def about(request):
    return HttpResponse('About us')

def coin(request):
    return HttpResponse(random.choice(['Орел', 'Решка']))

def cube(request):
    return HttpResponse(random.randint(1,6))

def number(request):
    return HttpResponse(random.randint(0,100))

# for sem2:
# Создайте модель для запоминания бросков монеты: орёл или  решка.
# Также запоминайте время броска
def game(request):    
    game = Game(state=random.choice(['orel','reshka'])) 
    game.save()   # что это значит ??????
    return HttpResponse(game)

# Доработаем задачу 1.
# Добавьте статический метод для статистики по n последним
# броскам монеты.
# Метод должен возвращать словарь с парой ключейзначений, для орла и для решки.
# see models.py, class Game
def statistic(request):
    n = 5
    return HttpResponse(Game.statistic(n))