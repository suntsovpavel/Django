from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import LoginForm, RecipeForm
from datetime import datetime
from django.core.files.storage import FileSystemStorage

from .models import MyUser, Recipe, Category

def index(request):    
    return render(request, 'myapp/index.html', {'title': 'Главная', 
                                                'user': request.user,
                                                'content': [{ x.name: x.name } for x in Category.objects.all()]})

# Страница авторизации
def my_login(request):
    # !!! Если авторизованный пользователь вошел на страницу авторизации - отменяем авторизацию:
    if request.user.is_authenticated:
        logout(request)

    if request.method == 'POST':
        form = LoginForm(request.POST)               
        if form.is_valid():    
            username = form.cleaned_data['name']    
            password = form.cleaned_data['password']    
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Проверяем, внесен ли пользователь в список MyUser. Если нет - добавляем
                myUser = MyUser.objects.filter(username=username).first()
                if myUser is None:
                    myUser = MyUser(username=username, date_register=datetime.now())
                    myUser.save()
                return redirect('/')                
            else:
                message = 'Логин либо пароль некорректны!' 
        else:
            message = 'Некорректный формат введенных данных!'                
    else:
        message = 'Введите логин и пароль'
        form = LoginForm()
    return render(request, 'myapp/login.html', {'title': 'Авторизация', 
                                                'message': message,
                                                'form':form})

# Страница регистрации 
# Используем готовую форму ввода данных регистрации UserCreationForm
def my_reg(request):    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():    
            form.save()
            username = form.cleaned_data['username']    
            password = form.cleaned_data['password1']    
            user = authenticate(request, username=username, password=password)
            login(request, user)
            myUser = MyUser(username=username, date_register=datetime.now())
            myUser.save()
            return redirect('/')
        else:
            message = 'Некорректный формат введенных данных!'                
    else:
        message = 'Регистрация нового пользователя'
        form = UserCreationForm()
    return render(request, 'myapp/reg.html', {'title': 'Регистрация', 
                                                'message': message,
                                                'form':form})

# Страница выхода (де-авторизации)
def my_logout(request): 
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

# Страница добавления рецепта
# Доступна только для авторизованного пользователя
def add_recipe(request):
    # Неавторизованных пользователей перебрасываем на страницу авторизации:
    if not request.user.is_authenticated:
        return redirect('/login/')
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)     
        if form.is_valid():   
            myUser = MyUser.objects.filter(username=request.user.username).first()
            if myUser is None:
                return HttpResponse(f'!!! Пользователь {request.user.username} отсутствует в базе!!!')
            else:                        
                name = form.cleaned_data['name']    
                desc = form.cleaned_data['desc']    
                cooking_steps = form.cleaned_data['cooking_steps']    
                time_cooking = form.cleaned_data['time_cooking']    
                category = form.cleaned_data['category']    
                image = form.cleaned_data['image']  
                fs = FileSystemStorage()
                fs.save(image.name, image)

                if len(category) > 0:
                    recipe = Recipe(author=myUser,
                                    name=name,
                                    desc=desc,
                                    cooking_steps=cooking_steps,
                                    time_cooking=time_cooking,
                                    image=image,
                                    date = datetime.now())    
                    recipe.save()
                    for name in category:
                        c = Category.objects.filter(name=name).first()
                        recipe.categories.add(c)
                    message = 'Рецепт успешно добавлен!' 
                else:
                    message = 'Выберите как минимум одну категорию!'    
        else:
            message = 'Некорректные данные'    
    else:
        message = 'Заполните форму'
        form = RecipeForm()        
    return render(request, 'myapp/add_recipe.html', {'title': 'Новый рецепт', 
                                                    'message': message,
                                                    'form':form})   


# Страница редактирования рецепта
# Доступна только для авторизованного пользователя, который является автором рецепта
# @login_required
# def edit_recipe_by_name(request, name: str):




# вспомогательная таблица категорий
def fill_categories(request):  
    c = Category.objects.last()  
    while c is not None: # удаляем все существующие записи в БД
        c.delete()
        c = Category.objects.last()         

    categories = ['выпечка',
                  'мясная продукция',
                  'молочная продукция',
                  'сыроедение',
                  'вегетарианство',
                  'салаты',
                  'супы',
                  'легкие закуски']
    i=0
    for name in categories:
        cat = Category(name=name, desc=f'some description{i}')
        cat.save()
        i += 1
    return redirect('/')
