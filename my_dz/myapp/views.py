from django.shortcuts import render
from django.http import HttpResponse
from .models import Order, User, Product
import logging
import datetime

logger = logging.getLogger(__name__)

# 1. Создайте пару представлений в вашем первом приложении:
# — главная
# — о себе.
# Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.
# Сохраняйте в логи данные о посещении страниц.

def index(request):
    logger.info('Index page accessed')
    return render(request, "myapp/index.html")

def about(request):
    logger.info('about page accessed')
    return render(request, "myapp/about.html")

# ДЗ 3
# Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
# — за последние 7 дней (неделю)
# — за последние 30 дней (месяц)
# — за последние 365 дней (год)
# Товары в списке не должны повторяться.
def list_orders(request, pk_user: int):
    user = User.objects.filter(pk=pk_user).first()
    if user is not None:    
        # заказы пользователя:
        orders = Order.objects.filter(customer=user) 
        orders.reverse()

        data_week = []
        exists_products: Product = []   # исключаем повторение продуктов
        for order in orders:
            if order.date_ordered < (datetime.date.today() - datetime.timedelta(days=7)):
                continue
            for product in order.products.all():
                if not product in exists_products:
                    data_week.append(f'name: {product.name}, date: {order.date_ordered}') 
                    exists_products.append(product)        

        # for 30 days:       
        data_month = []
        exists_products: Product = []   # исключаем повторение продуктов
        for order in orders:
            if order.date_ordered < (datetime.date.today() - datetime.timedelta(days=30)):
                continue
            for product in order.products.all():
                if not product in exists_products:
                    data_month.append(f'name: {product.name}, date: {order.date_ordered}') 
                    exists_products.append(product)  

        # for 365 days                                
        data_year = []
        exists_products: Product = []   # исключаем повторение продуктов
        for order in orders:
            if order.date_ordered < (datetime.date.today() - datetime.timedelta(days=365)):
                continue
            for product in order.products.all():
                if not product in exists_products:
                    data_year.append(f'name: {product.name}, date: {order.date_ordered}') 
                    exists_products.append(product)           

        context = {'data_week': data_week,
                   'data_month': data_month,
                   'data_year': data_year }        
    # else:
    #     context = {'content': 'Пользователь не найден'}
    return render (request, 'myapp/list_orders.html', context)
