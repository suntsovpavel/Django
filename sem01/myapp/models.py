from django.db import models

class Game(models.Model):
    state = models.CharField(max_length=100)   # варианты: орел, решка
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'state: {self.state}, time: {self.time}'

# Добавьте статический метод для статистики по n последним
# броскам монеты.
# Метод должен возвращать словарь с парой ключейзначений, для орла и для решки.
    @staticmethod
    def statistic(n: int):    
        games = Game.objects.all()
        if (len(games)>n): 
            games=games[len(games)-n:]
        return games

class Author(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField(max_length=2000)
    birthday = models.DateField(blank=False)

    def fullname(self):
        return self.name + ' ' + self.lastname 
    

