from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from io import StringIO
from django.utils import timezone
from django.db import transaction
from pharmacy_app.models import Pracownik
from pharmacy_app.models import Apteka


class Command(BaseCommand):
    help = 'register pharmacy'

    def add_arguments(self, parser):
        parser.add_argument('admin_login', type= str, help= '')
        parser.add_argument('admin_token', type= str, help= '')
        parser.add_argument('nazwa', type= str, help= '')
        parser.add_argument('adres', type= str, help= '')
        parser.add_argument('kod_pocztowy', type= str, help= '')
        
    def handle(self, *args, **kwargs):
        with transaction.atomic():
            _login = kwargs['admin_login']
            _token = kwargs['admin_token']
            try:
                call_command('autoryzacja_pracownik', _login, _token)
            except:
                raise CommandError('Authorization error!')
            else:
                _apteka = Apteka(nazwa= kwargs['nazwa'], adres = kwargs['adres'], kod_pocztowy = kwargs['kod_pocztowy'])
                _apteka.save()
            return 0
