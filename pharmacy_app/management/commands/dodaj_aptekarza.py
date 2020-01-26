from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from pharmacy_app.models import Pracownik
from django.core.management import call_command
from io import StringIO
from django.db import transaction
from polls.management.commands.logowanie import hash_password_p, hash_password


class Command(BaseCommand):
    help = 'Create users'

    def add_arguments(self, parser):
        parser.add_argument('login', type=str, help='')
        parser.add_argument('haslo', type=str, help='')

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            login = kwargs['login']
            haslo = kwargs['haslo']
            pracownik, _ = Pracownik.objects.get_or_create(login=login)
            pracownik.poziom_dostepu = 2
            hash_password(pracownik, haslo)
            return
            # try:
            #     call_command('autoryzacja_pracownik',_login, _token)
            # except:
            #     raise CommandError('Authorization error!')
            # try:
            #     _passwd = kwargs['pass_h']
            #     _pracownik = Pracownik(login=kwargs['login_h'], poziom_dostepu= int(kwargs['level_h']))
            #     hash_password(_pracownik, _passwd)
            # except:
            #     raise CommandError('new user except')
            # return 0
