from django.core.management.base import BaseCommand
from myapp.models import User, Product, Order 
import random
import datetime
import decimal

class Command(BaseCommand):
    help = "Fill tables users,products,orders by fake data."

    NUM_PRODUCTS = 20
    NUM_ORDERS = 100

    def add_arguments(self, parser):
        parser.add_argument('num_users', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        num_users = kwargs.get('num_users')

        for i in range(num_users):
            user = User(name=f'Name{i}', 
                        email=f'mail{i}@mail.ru',
                        phone = random.randint(80000000, 89999999),
                        password =f'password{i}',
                        adress = f'some_adress{i}',
                        date_register = datetime.date(2022,1,1)) 
            user.save()

        for i in range(self.NUM_PRODUCTS):
            prod = Product(name=f'name{i}', 
                            description =f'some description{i}', 
                            price = decimal.Decimal(1. + 99. * random.random()),                                                          
                            amount = random.randint(10,1000),
                            date = datetime.date(2022,1,1)) 
            prod.save()

        # Составляем какой-то список дат покупок, чтоб потом делать выборки за последнюю неделю и т.п.
        dates = [datetime.date(2023,1,1),
                 datetime.date(2023,6,1),
                 datetime.date(2023,12,1),
                 datetime.date(2024,2,1),
                 datetime.date(2024,4,1),
                 datetime.date(2024,4,10),
                 datetime.date(2024,4,20),
                 datetime.date(2024,5,1),
                 datetime.date(2024,5,5),
                 datetime.date(2024,5,10),
                 datetime.date(2024,5,15)]
        for date in dates:
            num_products = random.randint(3,15)   # в заказе от 3 до 15 позиций товаров
            products = [random.choice(Product.objects.all()) for _ in range(num_products)]
            total_price=0
            for p in products:
                total_price += p.price
            order = Order(customer = random.choice(User.objects.all()),  # cвыбираем случайного пользователя из имеющихся                          
                        date_ordered = date,
                        total_price = total_price)
            order.save()
            for p in products:
                order.products.add(p)
            
