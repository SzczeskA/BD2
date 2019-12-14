from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from pharmacy_app.models import Pracownik
from pharmacy_app.models import Apteka



class Command(BaseCommand):
    help = 'register pharmacy'

    def add_arguments(self, parser):
        parser.add_argument('admin', type=Pracownik, help='login aptekarza')
        parser.add_argument('pharmacy', type=Ateka, help='haslo aptekarza')
        
    def handle(self, *args, **kwargs):
        admin = kwargs['admin']
        out = StringIO()
        call_command('worker_login', admin, stdout= out)
        if int(out.getvalue()) != 0:
            raise CommandError('Authorization error!')
            #return 1
        else:
            apteka= kwargs['apteka']
            apteka.save()
        return 0
