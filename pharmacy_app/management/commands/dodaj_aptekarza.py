from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from pharmacy_app.models import Pracownik

class Command(BaseCommand):
    help = 'Create users'

    def add_arguments(self, parser):
        parser.add_argument('admin_login', type=str, help='')
        parser.add_argument('admin_token', type=str, help='')
        parser.add_argument('new_user', type=Pracownik, help='user to create')

    def handle(self, *args, **kwargs):
        _login = kwargs['admin_login']
        _token = kwargs['admin_token']
        out = StringIO()
        try:
            call_command('autoryzacja_pracownik',_login, _token, stdout= out)
        except:
        #if int(out.getvalue()) != 0:
            raise CommandError('Authorization error!')
            #return 1
        try:
            #login, mail, pass_len exceptions 
            _user = kwargs['new_user']
            #_worker.hash_hasla=__hash(_worker.hash_hasla)
            _user.save()
        except:
            raise CommandError('new user except')
            #return 1
        return 0
