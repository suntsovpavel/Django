from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('about/', views.about, name='about'),
 path('coin/<int:num>/', views.coin, name='coin'),
 path('cube/<int:num>/', views.cube, name='cube'),
 path('number/<int:num>/', views.number, name='number'),
 # sem2:
 path('game/', views.game, name='game'),
 path('statistic/', views.statistic, name='statistic'),
 path('create_authors/', views.create_authors, name='create_authors'),
 path('form_games/', views.form_games, name='form_games'),
]