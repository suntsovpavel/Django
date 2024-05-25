from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'myapp/index.html', {'title': 'Главная', 
                                                'user': request.user,
                                                'content': 'Пока ничего'})

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
                return redirect('/')
            else:
                message = 'Такого пользователя нет в базе' 
        else:
            message = 'Некорректный формат введенных данных'                
    else:
        message = 'Введите логин и пароль'
        form = LoginForm()
    return render(request, 'myapp/login.html', {'title': 'Авторизация', 
                                                'message': message,
                                                'form':form})

# Страница регистрации 
# Используем готовую форму ввода данных при регистрации UserCreationForm
def my_reg(request):    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():    
            form.save()
            username = form.cleaned_data['username']    
            password = form.cleaned_data['password1']    
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            message = 'Некорректный формат введенных данных'                
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

