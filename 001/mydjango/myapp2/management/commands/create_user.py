from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        user = User(name='Django', email='john@example.com', password='secret', age=75)
        user.save()
        self.stdout.write(f'{user}')