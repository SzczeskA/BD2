from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from clients.models import Klient



class Command(BaseCommand):
    help = 'Create  users'

    def add_arguments(self, parser):
        parser.add_argument('login', type=str, help='login klienta')
        parser.add_argument('haslo', type=str, help='haslo klienta')
        parser.add_argument('-t','--token', type=str, help='token klienta')
        
    def handle(self, *args, **kwargs):
        #if Token, login, in log_table #perm_granted
        #_klient=Klient.objects.get(login=kwargs['login'])
        #_hash= __hash(kwargs['haslo'])
        #if _hash== _klient.hash
            #add (_klient, Token, time) to log_table
            #perm_granted
        #else rise.error(wrong_passw)

