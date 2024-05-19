from django.core.management.base import BaseCommand
from myapp.models import User
from datetime import datetime

class Command(BaseCommand):
    help = "Create user."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone', type=int)
        parser.add_argument('adress', type=str)

    def handle(self, *args, **kwargs):
        user = User(name=kwargs['name'], 
                    email=kwargs['email'],            
                    phone=kwargs['phone'],
                    password='secret', 
                    adress=kwargs['adress'],
                    date_register=datetime.now())
        user.save()
        self.stdout.write(f'{user}')