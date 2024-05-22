from django.shortcuts import render
from django.http import HttpResponse
import os

from my_dz.settings import MEDIA_ROOT

from .models import Order, User, Product
import logging
import datetime
from django.core.files.storage import FileSystemStorage
from .forms import ProductForm, ProductFormWithPK

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

def inner_list_orders(orders: list[Order],
                      date_limit: datetime.date):   # дата, ранее которой заказы не рассматриваются 
    used_orders = []
    used_products = []
    result = []
    while len(used_orders) < len(orders):
        # ищем самый поздний заказ вне списка used_orders
        order = None
        for ord in orders:
            if ord not in used_orders and (order == None or ord.date_ordered > order.date_ordered):
                order = ord   

        if order.date_ordered < date_limit:
            break                             

        for product in order.products.all():
            if not product in used_products:    
                result.append(f'name: {product.name}, date order: {order.date_ordered}')     
                used_products.append(product)
        used_orders.append(order)                
    return result

# ДЗ 3
# Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
# — за последние 7 дней (неделю)
# — за последние 30 дней (месяц)
# — за последние 365 дней (год)
# Товары в списке не должны повторяться. 
def list_orders(request, pk_user: int):
    user = User.objects.filter(pk=pk_user).first()
    if user is not None:            
        orders = Order.objects.filter(customer=user)         

        context = {'incorrect_user': False,
                    'data_week': inner_list_orders(orders, (datetime.date.today() - datetime.timedelta(days=7))),
                   'data_month': inner_list_orders(orders, (datetime.date.today() - datetime.timedelta(days=30))),
                   'data_year': inner_list_orders(orders, (datetime.date.today() - datetime.timedelta(days=365))), 
                   }        
    else:
        context = {'incorrect_user': True}
    return render (request, 'myapp/list_orders.html', context)

# ДЗ 4
# 1. Доработаем задачу про клиентов, заказы и товары из прошлого семинара.
# Создайте форму для редактирования товаров в базе данных.
# 2. Измените модель продукта, добавьте поле для хранения фотографии продукта.
# Создайте форму, которая позволит сохранять фото.
def show_product(request, pk):
    product = Product.objects.filter(pk=pk).first()
    if product is not None:            
        context = {'incorrect_product': False,
                   'name': product.name,  
                    'description': product.description,
                    'price':  product.price,
                    'amount': product.amount, 
                    'date': product.date, 
                    'path_image': str(os.path.join(MEDIA_ROOT, product.image)) }  # not works...
    else:
        context = {'incorrect_product': True}                
    return render (request, 'myapp/show_product.html', context)  

def edit_product(request):    
    if request.method == 'POST':
        form = ProductFormWithPK(request.POST, request.FILES)       
        if form.is_valid():
            pk = form.cleaned_data['pk']    
            product = Product.objects.filter(pk=pk).first()
            if product is None:
                message = 'Такого товара в БД не имеется'
            else:                        
                name = form.cleaned_data['name']    
                description = form.cleaned_data['description']    
                price = form.cleaned_data['price']    
                amount = form.cleaned_data['amount']    
                date = form.cleaned_data['date']
                image = form.cleaned_data['image']  
                fs = FileSystemStorage()
                fs.save(image.name, image)

                product.name = name
                product.description = description
                product.price = price
                product.amount = amount
                product.date = date
                product.image = image.name
                product.save()
                message = 'Товар успешно изменен'
        else:
            message = 'Некорректные данные'    
    else:
        message = 'Заполните форму'
        form = ProductFormWithPK()
    return render(request, 'myapp/edit_product.html', {'title': 'edit_product', 
                                                    'message': message,
                                                    'form':form})     

def add_product(request):    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)               
        if form.is_valid():    
            name = form.cleaned_data['name']    
            description = form.cleaned_data['description']    
            price = form.cleaned_data['price']    
            amount = form.cleaned_data['amount']    
            date = form.cleaned_data['date'] 
            image = form.cleaned_data['image']  
            fs = FileSystemStorage()
            fs.save(image.name, image)

            product = Product(name = name,description = description,price = price,amount = amount,date = date,image = image.name)
            product.save()
            message = 'Товар успешно добавлен' 
        else:
            message = 'Некорректные данные'                
    else:
        message = 'Заполните форму'
        form = ProductForm()
    return render(request, 'myapp/edit_product.html', {'title': 'add_product', 
                                                    'message': message,
                                                    'form':form})

