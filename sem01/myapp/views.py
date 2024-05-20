from django.shortcuts import render
from django.http import HttpResponse
import random
import logging
from .models import Game, Author
from datetime import date

logger = logging.getLogger(__name__)

# sem3
# Изменяем задачу 8 из семинара 1 с выводом двух html страниц:
# главной и о себе.
# Перенесите вёрстку в шаблоны.
# Представления должны пробрасывать полезную информацию в
# шаблон через контекст.
def index(request):
    context = {
        'title': 'Главная',
        'header': 'Главная',
        'content': 'lorenbv ncvbncvb ncbv cvbncvfb gkj ygiuygtiuygkjhb giouygouyg uhoiuh'  
    }
    return render(request, 'myapp/index.html', context)

def about(request):
    context = {
        'title': 'обо мне',
        'header': 'Обо мне',
        'content': 'вфыва ывапорпролп ффывафыв пролпролпрола арвпарвапр вапрвапрвапрвпарююююю.....'  
    }
    return render(request, 'myapp/index.html', context)

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

# sem 3
# Доработаем задачу 7 из урока 1, где бросали монетку,
# игральную кость и генерировали случайное число.
# Маршруты могут принимать целое число - количество
# бросков.
# Представления создают список с результатами бросков и
# передают его в контекст шаблона.
# Необходимо создать универсальный шаблон для вывода
# результатов любого из трёх представлений.
def coin(request, num: int):
    result = [random.choice(['Орел', 'Решка']) for _ in range(num)]
    context = {'title': 'Орел и Решка',
               'content' : result}
    return render (request, 'myapp/games.html', context)

def cube(request, num: int): 
    result = [random.randint(1,6) for _ in range(num)]
    context = {'title': 'Игральная кость',
               'content' : result}
    return render (request, 'myapp/games.html', context)

def number(request, num: int):
    result = [random.randint(0,100) for _ in range(num)]
    context = {'title': 'Случаное число 0 - 100',
               'content' : result}
    return render (request, 'myapp/games.html', context)

# sem3
# Создайте модель Статья (публикация). 
# Авторы из прошлой задачи могут писать статьи. 
# У статьи может быть только один автор. 
# У статьи должны быть следующие обязательные поля:
# ○ заголовок статьи с максимальной длиной 200 символов
# ○ содержание статьи
# ○ дата публикации статьи
# ○ автор статьи с удалением связанных объектов при удалении автора
# ○ категория статьи с максимальной длиной 100 символов
# ○ количество просмотров статьи со значением по умолчанию 0
# ○ флаг, указывающий, опубликована ли статья, со значением по умолчанию False

# Доработаем задачи из прошлого семинара по созданию моделей автора, статьи и комментария.
# Создайте шаблон для вывода всех статей автора в виде списка заголовков.
# * Если статья опубликована, заголовок должен быть ссылкой на статью.
# * Если не опубликована, без ссылки.
# Не забываем про код представления с запросом к базе данных и маршруты.
