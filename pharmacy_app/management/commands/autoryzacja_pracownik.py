from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone
from datetime import datetime, timedelta
from django.db import transaction
from pharmacy_app.models import Pracownik
from pharmacy_app.models import LogAutoryzacja


class Command(BaseCommand):
    help = 'register pharmacy'

    def add_arguments(self, parser):
        parser.add_argument('admin_login', type= str, help= '')
        parser.add_argument('admin_token', type= str, help= '')
        
    def handle(self, *args, **kwargs):
        with transaction.atomic():
            _login = kwargs['admin_login']
            _token = kwargs['admin_token']
            _log = LogAutoryzacja.objects.get(login=_login)
            _time = _log.data_autoryzacji
            _time =_time + timedelta(minutes=15)
            _now = datetime.now()+ timedelta(minutes=0)
            if _log.token == _token: #and _time > _now:
                #_log.data_autoryzacji = datetime.now()  ##timezone
                #_log.update(data_autoryzacji = datetime.now())
                print('aut')
            else:
                raise CommandError('nieautoryzowany dostep')
