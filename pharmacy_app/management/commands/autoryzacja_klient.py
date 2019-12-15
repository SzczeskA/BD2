from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from datetime import datetime
from clients.models import Klient
from clients.models import LogAutoryzacja


class Command(BaseCommand):
    help = 'register pharmacy'

    def add_arguments(self, parser):
        parser.add_argument('user_login', type=str, help='')
        parser.add_argument('user_token', type=str, help='')
        
    def handle(self, *args, **kwargs):
        _login = kwargs['admin_login']
        _token = kwargs['admin_token']
        _log = LogAutoryzacja.objects.get(login= _login)
        _time = _log.data_autoryzacji.time.minute + 15
        if _log.token= _token and _time < datetime.now():##timezone
           _log.data_autoryzacji = datetime.now()##timezone
           _log.update()
           return 0 
        else:
            raise CommandError('nieautoryzowany dostep')
        return 1
