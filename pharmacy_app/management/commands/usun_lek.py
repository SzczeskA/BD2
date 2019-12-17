from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from pharmacy_app.models import Pracownik
from pharmacy_app.models import Lek



class Command(BaseCommand):
    help = 'Create users'

    def add_arguments(self, parser):
        parser.add_argument('admin_login', type=str, help='')
        parser.add_argument('admin_token', type=str, help='')
        parser.add_argument('remove_drug', type=int, help='Lek ID')
        #parser.add_argument('remove_user', type=str, help='Pracownik login')

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            _login = kwargs['admin_login']
            _token = kwargs['admin_token']
            out = StringIO()
            try:
                call_command('autoryzacja_pracownik',_login, _token, stdout= out)
            except:
            #if int(out.getvalue()) != 0:
                #return 1
                raise CommandError('Authorization error!')
            try:
                _drug = Lek.objects.get(pk=int(kwargs['remove_drug'])
                _drug.delete()
            except:
                raise CommandError('drug doesnt exist')
                #return 1
            return 0
