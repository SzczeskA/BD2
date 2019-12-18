from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from datetime import datetime
from django.utils import timezone
from clients.models import Klient
from clients.models import LogAutoryzacja
from polls.management.commands.logowanie import check_password
from pharmacy_app.management.commands.Token import genToken


class Command(BaseCommand):
    help = 'Login apothecary'

    def add_arguments(self, parser):
        parser.add_argument('login', type=str, help='login')
        parser.add_argument('haslo', type=str, help='haslo')

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            _login = kwargs['login']
            _haslo = kwargs['haslo']
            try:
                _klient = Klient.objects.get(login=_login)
            except:
                raise CommandError('Wrong Login')
            if check_password(_klient, _haslo):
                _token = genToken()
                try:
                    _ulog = LogAutoryzacja.objects.get(login=_login)
                    _ulog.token = _token
                    _ulog.update()
                    return _token
                except:
                    _log = LogAutoryzacja(login=_login, token=_token, data_autoryzacji=datetime.now())
                    _log.save()
                    return _token
            else:
                raise CommandError('wrong password')