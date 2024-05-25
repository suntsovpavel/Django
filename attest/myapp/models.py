from django.db import models

class MyUser(models.Model):
    username = models.CharField(max_length=100)
    date_register = models.DateField()

    def __str__(self):
        return f'Username: {self.name}, date_register: {self.date_register}'

# Категории рецептов:
# ○ Название
# ○ *другие поля на ваш выбор
class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return f'name: {self.name}, description:{self.desc}'
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)   

    def __str__(self):
        return f'name: {self.name}'   
    
# модель Рецепт:
# - Автор(пользователь)
# - Название
# - Описание
# - Шаги приготовления
# - Время приготовления
# - дата создания/последней редакции
# - Изображение
# - список категорий
class Recipe(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)        
    name = models.CharField(max_length=100)
    desc = models.TextField()
    cooking_steps = models.TextField()
    time_cooking = models.TimeField()    
    date = models.DateField()       # дата создания либо последней редакции 
    image = models.ImageField() 
    categories = models.ManyToManyField(Category)

    def __str__(self):
        splited = self.desc.split()        
        return f'name: {self.name}, desc(short): "{splited[:10]+'...' if len(splited)>10 else splited}", by author: {self.author}'     