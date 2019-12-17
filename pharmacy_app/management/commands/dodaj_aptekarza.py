from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from pharmacy_app.models import Pracownik

class Command(BaseCommand):
    help = 'Create users'

    def add_arguments(self, parser):
        parser.add_argument('admin_login', type=str, help='')
        parser.add_argument('admin_token', type=str, help='')
        parser.add_argument('new_user', type=Pracownik, help='user to create')
        parser.add_argument('pass_h', type= str, help='')
        parser.add_argument('login_h', type= str, help='')
        parser.add_argument('level_h', type= str, help='')
        parser.add_argument('-p', '--pharm', type= str, help='')

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
            # _pass_h= BinaryField(kwargs['pass_h'])
            passwd = kwargs[pass_h]
            passwd = _hash(passwd)
            _user_h = Pracownik(hash_hasla=passwd, login=kwargs[login_h], poziom_dostepu=int(kwargs[level_h]))
            _user.save()
            _user.add(int(kwargs['-p']))
            _user.save()
        except:
            raise CommandError('new user except')
        return 0
