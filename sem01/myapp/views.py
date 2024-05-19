from django.shortcuts import render
from django.http import HttpResponse
import random
import logging
from .models import Game, Author
from datetime import date

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
# 1. Создайте модель для запоминания бросков монеты: орёл или  решка.
# Также запоминайте время броска
def game(request):    
    game = Game(state=random.choice(['orel','reshka'])) 
    game.save()   # что это значит ??????
    return HttpResponse(game)

# 2. Доработаем задачу 1.
# Добавьте статический метод для статистики по n последним
# броскам монеты.
# Метод должен возвращать словарь с парой ключейзначений, для орла и для решки.
# see models.py, class Game
def statistic(request):
    n = 5
    return HttpResponse(Game.statistic(n))

# 3. Создайте модель Автор. Модель должна содержать
# следующие поля:
# ○ имя до 100 символов
# ○ фамилия до 100 символов
# ○ почта
# ○ биография
# ○ день рождения
# Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.
# see models.py, class Author
def create_authors(request):
    result = []
    for i in range(10):
        author = Author(name=f'name{i}',
                        lastname=f'lastname{i}',
                        biography=f'biography{i}',
                        birthday=date.today())
        author.save()
        result.append(author.fullname())
    return HttpResponse(f'{result}')        