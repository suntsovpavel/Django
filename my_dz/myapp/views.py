from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Создайте пару представлений в вашем первом приложении:
# — главная
# — о себе.
# Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.
# Сохраняйте в логи данные о посещении страниц.

def index(request):
    html = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- <link rel="stylesheet" href="style.css" /> -->
  </head>
  <body>
    <a class="menu" href="/">Главная</a>
    <a class="menu" href="/about">Обо мне</a>
    <h1>Главная</h1>
    <p class="paragraf">
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis qui
      quidem et nostrum expedita repudiandae adipisci! Optio odio excepturi
      tempora dolore quas quae sed aut accusantium, deserunt obcaecati esse
      debitis.
    </p>
    <h2>Заголовок 2-го уровня</h2>
    <p class="paragraf">
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Non sunt dolores
      voluptates deserunt repellendus laborum dolorum ipsa hic nostrum, incidunt
      saepe necessitatibus numquam voluptas ducimus esse repudiandae natus,
      ipsum quisquam!
    </p>
    <p class="paragraf">
      Lorem ipsum dolor sit, amet consectetur adipisicing elit. Aliquam deserunt
      veniam possimus libero odio optio veritatis dolorem dolores maiores
      quibusdam neque, pariatur exercitationem adipisci labore, quas illo nisi
      nihil fugiat.
    </p>
    <p class="paragraf">
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque, aliquam
      voluptatum aliquid quo consectetur dolorum quidem suscipit eius facere
      accusamus soluta perspiciatis nesciunt vero dolor earum pariatur.
      Quisquam, soluta? Laudantium?
    </p>
  </body>
</html>
'''
    logger.info('Index page accessed')
    return HttpResponse(html)

def about(request):
    html = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- <link rel="stylesheet" href="style.css" /> -->
  </head>
  <body>
    <a class="menu" href="/">Главная</a>
    <a class="menu" href="/about">Обо мне</a>
    <h1>Обо мне</h1>
    <p class="paragraf">
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque, aliquam
      voluptatum aliquid quo consectetur dolorum quidem suscipit eius facere
      accusamus soluta perspiciatis nesciunt vero dolor earum pariatur.
      Quisquam, soluta? Laudantium?
    </p>
  </body>
</html>
'''
    logger.info('about page accessed')
    return HttpResponse(html)
