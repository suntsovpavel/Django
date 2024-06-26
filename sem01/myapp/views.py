from django.shortcuts import redirect, render
from django.http import HttpResponse
import random
import logging
from .models import Game, Author
from datetime import date
from .forms import GamesForm, AuthorForm

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
    
# sem 3
# Доработаем задачу 7 из урока 1, где бросали монетку,
# игральную кость и генерировали случайное число.
# Маршруты могут принимать целое число - количество бросков.
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

# sem4
# Доработаем задачу про броски монеты, игральной кости и случайного числа.
# Создайте форму, которая предлагает выбрать: монета, кости, числа.
# Второе поле предлагает указать количество попыток от 1 до 64.
def form_games(request):
    if request.method == 'POST':
        form = GamesForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data['game_type']
            num_tries = form.cleaned_data['num_tries']
            print(f'game_type: {game_type}, num_tries: {num_tries}')
            # задействуем созданные ранее функции
            if game_type == 'coin':
                return coin(request, num_tries) 
            elif  game_type == 'cube':
                return cube(request, num_tries)                
            else:
                # return number(request, num_tries)    
                return redirect(number, num_tries)
    else:
        form = GamesForm()                                   
    return render(request, 'myapp/all_games.html', {'title': 'games 3 in 1', 'form':form})



# 3. Создайте модель Автор. Модель должна содержать следующие поля:
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

# sem4
# Продолжаем работу с авторами, статьями и комментариями.
# Создайте форму для добавления нового автора в базу данных.
# Используйте ранее созданную модель Author
def add_author(request):
    message = 'Некорректные данные'
    if request.method == 'POST':
        form = AuthorForm(request.POST)        
        if form.is_valid():
            name = form.cleaned_data['name']    
            lastname = form.cleaned_data['lastname']    
            email = form.cleaned_data['email']    
            biography = form.cleaned_data['biography']    
            birthday = form.cleaned_data['birthday'] 
            author = Author(name=name,
                            lastname=lastname,
                            email=email,
                            biography=biography,
                            birthday= birthday)
            author.save()
            message = 'Автор добавлен в БД'
    else:
        message = 'Заполните форму'
        form = AuthorForm()
    return render(request, 'myapp/add_author.html', {'title': 'add author in DB', 
                                                    'message': message,
                                                    'form':form})               

# sem3
# Создайте модель Статья (публикация). 
# Авторы из прошлой задачи могут писать статьи. 
# У статьи может быть только один автор. 
# У статьи должны быть следующие обязательные поля:
# ○ заголовок статьи с максимальной длиной 200 символов
# ○ содержание статьи
# ○ дата публикации статьи
# ○ автор статьи (с удалением связанных объектов при удалении автора)
# ○ категория статьи с максимальной длиной 100 символов
# ○ количество просмотров статьи со значением по умолчанию 0
# ○ флаг, указывающий, опубликована ли статья, со значением по умолчанию False

# Доработаем задачи из прошлого семинара по созданию моделей автора, статьи и комментария.
# Создайте шаблон для вывода всех статей автора в виде списка заголовков.
# * Если статья опубликована, заголовок должен быть ссылкой на статью.
# * Если не опубликована, без ссылки.
# Не забываем про код представления с запросом к базе данных и маршруты.
