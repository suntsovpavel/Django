from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth import authenticate, login

def index(request):
    return HttpResponse('Главная') # TO DO

def mylogin(request):    
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
                message = 'Этот пользователь не зарегистрирован, попробуйте еще раз' 
        else:
            message = 'Некорректный формат введенных данных'                
    else:
        message = 'Введите логин и пароль'
        form = LoginForm()
    return render(request, 'myapp/login.html', {'title': 'Авторизация', 
                                                'message': message,
                                                'form':form})
