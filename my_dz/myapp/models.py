from django.db import models

# Создайте три модели Django: клиент, товар и заказ.
# Клиент может иметь несколько заказов. 

# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    date_register = models.DateField(blank=False)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, phone: {self.phone},adress: {self.adress},date_register: {self.date_register}'

# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)    
    amount = models.IntegerField()
    date = models.DateField(blank=False)
    image = models.FilePathField(default='default_image.png')     

    def __str__(self):
        return f'name: {self.name}'

# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа
# Заказ может содержать несколько товаров. 
# Товар может входить в несколько заказов.
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)



