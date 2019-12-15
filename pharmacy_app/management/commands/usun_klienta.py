from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from clients.models import Klient



class Command(BaseCommand):
    help = 'Login apothecary'

    def add_arguments(self, parser):
        parser.add_argument('login', type=str, help='login')
        parser.add_argument('haslo', type=str, help='haslo')
        
    def handle(self, *args, **kwargs):
        _login= Klient.objects.get(login=kwargs['login'])
        _hash= __hash(kwargs['haslo'])
        try 
            _klient= Klient.objects.get(login= _login)
            _klient.delete()
            return 0
        else:
            raise CommandError('login exist but sth goes wrong')
            #return 2
        return 0

