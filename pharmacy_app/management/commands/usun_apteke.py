from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone
from pharmacy_app.models import Pracownik
from pharmacy_app.models import Apteka



class Command(BaseCommand):
    help = 'Create users'

    def add_arguments(self, parser):
        parser.add_argument('admin_login', type=str, help='')
        parser.add_argument('admin_token', type=str, help='')
        parser.add_argument('remove_apt', type=int, help='Apteka ID')

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            _login = kwargs['admin_login']
            _token = kwargs['admin_token']
            try:
                call_command('autoryzacja_pracownik',_login, _token, stdout= out)
            except:
            #if int(out.getvalue()) != 0:
                #return 1
                raise CommandError('Authorization error!')
            try:
                _apt = Apteka.objects.get(pk=int(kwargs['remove_pharm'])
                _apt.delete()
            except:
                raise CommandError('apthece doesnt exist')
                #return 1
            return 0
