from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from pharmacy_app.models import Pracownik
from pharmacy_app.models import Apteka



class Command(BaseCommand):
    help = 'register pharmacy'

    def add_arguments(self, parser):
        parser.add_argument('admin_login', type=str, help='')
        parser.add_argument('admin_token', type=str, help='')
        parser.add_argument('pharmacy', type=Apteka, help='')
        
    def handle(self, *args, **kwargs):
        _login = kwargs['admin_login']
        _token = kwargs['admin_token']
        out = StringIO()
        call_command('autoryzacja_pracownik',_login, _token, stdout= out)
        if int(out.getvalue()) != 0:
            raise CommandError('Authorization error!')
            #return 1
        else:
            apteka= kwargs['apteka']
            apteka.save()
        return 0
