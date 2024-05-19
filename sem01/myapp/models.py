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
        result = []
        games = Game.objects.all()
        if (len(games)>n): 
            games=games[len(games)-n:]
        for game in games:     
            result.append(game)
        return result

        

    

