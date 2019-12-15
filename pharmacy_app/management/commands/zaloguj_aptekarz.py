from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from pharmacy_app.models import Pracownik
from pharmacy_app.models import LogAutoryzacja



class Command(BaseCommand):
    help = 'Login apothecary'

    def add_arguments(self, parser):
        parser.add_argument('login', type=str, help='login aptekarza')
        parser.add_argument('haslo', type=str, help='haslo aptekarza')
        
    def handle(self, *args, **kwargs):
        _login=Pracownik.objects.get(login=kwargs['login'])
        _hash= __hash(kwargs['haslo'])
        _pracownik= Pracownik.objects.get(login= _login)
        if _hash== _pracownik.hash_hasla:
            #_token=generate()
            _log= LogAutoryzacja(login= _login, token=_token, data_autoryzacji=datetime.now())
            #send _token to user
            _log.save()
            return 0
        else:
            raise CommandError('wrong password')
            #return 2
        return 0

