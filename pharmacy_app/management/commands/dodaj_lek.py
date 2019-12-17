from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from pharmacy_app.models import Pracownik
from pharmacy_app.models import Lek



class Command(BaseCommand):
    help = 'register pharmacy'

    def add_arguments(self, parser):
        parser.add_argument('admin_login', type=str, help='')
        parser.add_argument('admin_token', type=str, help='')
        parser.add_argument('drug_name', type= str, help='')# nazwa-leku
        parser.add_argument('drug_country', type= str, help='')#kraj_pochodzenia
        parser.add_argument('drug_activeSub', type= str, help='')#substancje_czynne

    def handle(self, *args, **kwargs):
        _login = kwargs['admin_login']
        _token = kwargs['admin_token']
        out = StringIO()
        call_command('autoryzacja_pracownik', _login, _token, stdout= out)
        if int(out.getvalue()) != 0:
            raise CommandError('Authorization error!')
            #return 1
        else:
            _lek= Lek( kwargs['drug_name'], kwargs['drug_country'])# kwargs['drug_activeSub'])
            _lek.save()
            _lek.add(int(kwargs['drug_activeSub']))
            _lek.save()
        return 0
