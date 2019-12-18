from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from pharmacy_app.models import Pracownik
from pharmacy_app.models import Lek
from django.db import transaction
from django.core.management import call_command
from io import StringIO


class Command(BaseCommand):
    help = 'register pharmacy'

    def add_arguments(self, parser):
        parser.add_argument('admin_login', type=str, help='')
        parser.add_argument('admin_token', type=str, help='')
        parser.add_argument('drug_name', type= str, help='')# nazwa-leku
        parser.add_argument('drug_country', type= str, help='')#kraj_pochodzenia
        parser.add_argument('-a','--activeSub', type= str, help='')#substancje_czynne

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            _login = kwargs['admin_login']
            _token = kwargs['admin_token']
            try:
                call_command('autoryzacja_pracownik', _login, _token)
            except:
                raise CommandError('Authorization error!')
            else:
                _lek= Lek( nazwa=kwargs['drug_name'], kraj_pochodzenia=kwargs['drug_country'])# kwargs['drug_activeSub'])
                _lek.save()
                #_lek.add(substancje_czynne= int(kwargs['drug_activeSub']))
                #_lek.save()
            return 0
