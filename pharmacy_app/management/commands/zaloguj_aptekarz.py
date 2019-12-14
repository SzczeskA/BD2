from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from pharmacy_app.models import Pracownik



class Command(BaseCommand):
    help = 'Login apothecary'

    def add_arguments(self, parser):
        parser.add_argument('login', type=str, help='login aptekarza')
        parser.add_argument('haslo', type=str, help='haslo aptekarza')
        parser.add_argument('-t','--token', type=str, help='token aptekarza')
        
    def handle(self, *args, **kwargs):
        #if Token, login, in log_table:
            #perm_granted
        else:
            _aptekarz=Pracownik.objects.get(login=kwargs['login'])
            _hash= __hash(kwargs['haslo'])
            #if !login.exist()
                raise CommandError('wrong login')
                #return 1
            if _hash== _aptekarz.hash:
                #add (_aptekarz, Token, time) to log_table
                #perm_granted
            #else:
                raise CommandError('wrong password')
                #return 2
        return 0

