from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from pharmacy_app.models import Pracownik
from django.core.management import call_command
from io import StringIO
from django.db import transaction
from polls.management.commands.logowanie import hash_password_p

class Command(BaseCommand):
    help = 'Create users'

    def add_arguments(self, parser):
        parser.add_argument('admin_login', type=str, help='')
        parser.add_argument('admin_token', type=str, help='')
        parser.add_argument('pass_h', type= str, help='')
        parser.add_argument('login_h', type= str, help='')
        parser.add_argument('level_h', type= str, help='')
        parser.add_argument('-p', '--pharm', type= str, help='')

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            _login = kwargs['admin_login']
            _token = kwargs['admin_token']
            try:
                call_command('autoryzacja_pracownik',_login, _token)
            except:
                raise CommandError('Authorization error!')
            try:
                _passwd = kwargs['pass_h']
                _pracownik = Pracownik(login=kwargs['login_h'], poziom_dostepu= int(kwargs['level_h']))
                hash_password_(_pracownik, _passwd)
            except:
                raise CommandError('new user except')
            return 0
