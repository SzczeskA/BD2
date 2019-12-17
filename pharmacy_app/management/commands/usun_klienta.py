from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from clients.models import Klient



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
                if _klient.hash_hasla == _hash:
                    _klient.delete()
                return 0
            except:
                raise CommandError('login exist but sth goes wrong')


