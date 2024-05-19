from django.core.management.base import BaseCommand
from myapp.models import User

class Command(BaseCommand):
    help = "Update user name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone', type=int)
        parser.add_argument('adress', type=str)

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone=kwargs['phone']
        adress=kwargs['adress'],
        user = User.objects.filter(pk=pk).first()
        if user != None:
            user.name = name
            user.phone = phone
            user.email = email
            user.adress = adress
            user.save()
            self.stdout.write(f'{user}')