from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('login/', views.my_login, name='login'),
 path('reg/', views.my_reg, name='registration'),
 path('logout/', views.my_logout, name='logout'),
 path('add_recipe/', views.add_recipe, name='add_recipe'),
]