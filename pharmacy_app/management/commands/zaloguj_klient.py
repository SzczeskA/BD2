from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from clients.models import Klient
from clients.models import LogAutoryzacja



class Command(BaseCommand):
    help = 'Login apothecary'

    def add_arguments(self, parser):
        parser.add_argument('login', type=str, help='login')
        parser.add_argument('haslo', type=str, help='haslo')
        
    def handle(self, *args, **kwargs):
        with transaction.atomic():
            _login= Klient.objects.get(login=kwargs['login'])
            _hash= __hash(kwargs['haslo'])
            try:
                _klient= Klient.objects.get(login= _login)
            except:
                raise CommandError('Wrong Login')
            if _hash== _pracownik.hash_hasla:
                #_token=generate()
                _log= LogAutoryzacja(login= _login, token=_token, data_autoryzacji=datetime.now())
                #send _token to user
                _log.save()
                return 0
            else:
                raise CommandError('wrong password')
                #return 2

