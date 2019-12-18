from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from clients.models import Klient
from polls.management.commands.logowanie import check_password
from pharmacy_app.management.commands.Token import genToken
from django.core.management import call_command
from io import StringIO
from django.db import transaction


class Command(BaseCommand):
    help = 'Login apothecary'

    def add_arguments(self, parser):
        parser.add_argument('login', type=str, help='login')
        parser.add_argument('haslo', type=str, help='haslo')

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            _login=kwargs['login']
            _hash=kwargs['haslo']
            try:
                _klient = Klient.objects.get(login=_login)
            except:
                raise CommandError('Wrong Login')
            try:
                check_password(_klient, _hash)
            except:
                raise CommandError('Wrong Password')
            else:
                _klient.delete()



