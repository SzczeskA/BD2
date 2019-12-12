from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from pharmacy_app.models import Pracownik



class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('user', type=Pracownik, help='')

    def handle(self, *args, **kwargs):
        worker = kwargs['user']
        wroker.login();
        total=int(worker.pk)
        for i in range(total):
            print(i)
