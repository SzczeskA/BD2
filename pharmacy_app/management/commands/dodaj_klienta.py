from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.db import transaction
from django.db import IntegrityError
from pprint import pprint
from clients.models import Klient
from pharmacy_app.uzytkownicy import dodaj_klienta
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
        dodaj_klienta(**kwargs)



