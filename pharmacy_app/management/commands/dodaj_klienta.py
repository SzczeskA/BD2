from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.db import transaction
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
        parser.add_argument('-d', '--data', type=str, help='')
        parser.add_argument('login', type=str, help='')
        parser.add_argument('haslo', type=str, help='')

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            _klient = Klient(imie=kwargs['imie'], nazwisko=kwargs['nazwisko'], adres=kwargs['adres'], kod_pocztowy=kwargs['kod_pocztowy'], email=kwargs['email'], login=kwargs['login'], hash_hasla='')
            hash_password(client=_klient, password=kwargs['haslo'])
            print(kwargs['haslo'])
            pprint(vars(_klient))
            _klient.save()
            #_klient=Klient.objects.get(login=kwargs['user'])
            #if _klient.hash_hasla.length() < 8 rise.error("haslo")
            #_klient.hash_hasla=_hash(_klient.hash_hasla)
            #if(not _klient.save())

            #rise.error("login/mail used")

