from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from clients.models import Klient
from clients.models import LogAutoryzacja
from clients.management.commands import Token


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
                _token=genToken(14)
                _log= LogAutoryzacja(login= _login, token=_token, data_autoryzacji=datetime.now())
                _log.save()
                return _token
            else:
                raise CommandError('wrong password')
                #return 2

