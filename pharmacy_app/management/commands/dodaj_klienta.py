from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.db import transaction
from django.db import IntegrityError
from pprint import pprint
from clients.models import Klient
from polls.management.commands.logowanie import hash_password

class Command(BaseCommand):
    help = 'Create  users'

    def add_arguments(self, parser):
        parser.add_argument('imie', type=str, help='')
        parser.add_argument('nazwisko', type=str, help='')
        parser.add_argument('adres', type=str, help='')
        parser.add_argument('kod_pocztowy', type=str, help='')
        parser.add_argument('email', type=str, help='')
        parser.add_argument('login', type=str, help='')
        parser.add_argument('haslo', type=str, help='')

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            _log_u = Klient.objects.filter(login=kwargs['login'])
            _mail_u= Klient.objects.filter(email=kwargs['email'])
            if _log_u or _mail_u:
                raise CommandError('login or mail already used')
            _klient = Klient(imie=kwargs['imie'], nazwisko=kwargs['nazwisko'], adres=kwargs['adres'], kod_pocztowy=kwargs['kod_pocztowy'], email=kwargs['email'], login=kwargs['login'])
            #_klient.add(data_urodzenioa=kwargs['-d'])
            hash_password(client=_klient, password=kwargs['haslo'])
            print(kwargs['haslo'])
            pprint(vars(_klient))
            _klient.save()


