from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('about/', views.about, name='about'),
 path('list_orders/<int:pk_user>/', views.list_orders, name='list_orders'),
 path('edit_product/', views.edit_product, name='edit_product'),
]