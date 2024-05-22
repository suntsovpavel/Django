from django.contrib import admin
from .models import User, Product, Order

@admin.action(description='Сбросить описание товара')   
def reset_desc(modeladmin, request, queryset):
    queryset.update(description='')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'amount', 'date']
    ordering = ['-price', '-amount']
    list_per_page = 10
    search_fields = ['name']
    fieldsets = [
    (
        'О товаре',
        {
            'classes': ['wide'],
            'fields': ['name','description'],
        },
    ),
    (
        'Бухгалтерия',
        {
            'fields': ['price', 'amount'],
        }   
    ),
    (
        'Дата регистрации товара',
        {
            'fields': ['date'],
        }
    )    
    ]
    actions=[reset_desc]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'adress', 'date_register']
    ordering = ['name', 'date_register']
    list_per_page = 10
    search_fields = ['name']
    fieldsets = [
    (
        'Имя',
        {
            'fields': ['name'],
        },
    ),
    (
        'Контакты',
        {
            'fields': ['email', 'phone', 'adress'],
        }   
    ),
    (
        'Дата регистрации',
        {
            'fields': ['date_register'],
        }
    )    
    ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered', 'total_price']  # products не вывести, ибо many2many
    ordering = ['-date_ordered', 'total_price']
    list_per_page = 10
    fieldsets = [
    (
        'Заказчик',
        {
            'fields': ['customer'],
        },
    ),
    (
        'Дата заказа',
        {
            'fields': ['date_ordered'],
        }   
    ),
    (
        'Содержимое заказа',
        {
            'fields': ['products'],
        }        
    ),
    (
        'Итоговая стоимость',
        {
            'fields': ['total_price'],
        }
    )
    ]