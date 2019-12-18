from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from clients.models import Klient, Koszyk
from pharmacy_app.models import Pracownik, Opakowanie, Apteka, OpakowaniaApteki
from pharmacy_app.models import Lek
from django.db import transaction
from django.core.management import call_command
from io import StringIO


class Command(BaseCommand):
    help = 'register pharmacy'

    def add_arguments(self, parser):
        parser.add_argument('klient_login', type=str, help='')
        parser.add_argument('klient_token', type=str, help='')
        parser.add_argument('id_opakowania', type=str, help='')
        parser.add_argument('id_apteki', type=str, help='')
        parser.add_argument('ilosc', type=str, help='')

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            _login = kwargs['klient_login']
            _token = kwargs['klient_token']
            try:
                call_command('autoryzacja_klient', _login, _token)
            except:
                raise CommandError('Authorization error!')
            else:
                klient = Klient.objects.get(login=kwargs['klient_login'])
                opakowanie = Opakowanie.objects.get(pk=int(kwargs['id_opakowania']))
                if opakowanie is None:
                    raise Exception('Could not find the product!')
                apteka = Apteka.objects.get(pk=int(kwargs['id_apteki']))
                if apteka is None:
                    raise Exception('Could not find the pharmacy!')
                opakowanie_apteki = OpakowaniaApteki.objects.get(opakowanie=opakowanie, apteka=apteka)
                if opakowanie_apteki is None:
                    raise Exception('Could not find product in selected pharmacy!')
                try:
                    koszyk = Koszyk.objects.get(klient=klient, opakowanie=opakowanie, apteka=apteka)
                    koszyk.ilosc_opakowan += int(kwargs['ilosc'])
                    if opakowanie_apteki.ilosc < kwargs['ilosc']:
                        raise Exception('There is not enough product in selected pharmacy!')
                except:
                    koszyk= Koszyk(klient=klient, apteka=apteka, opakowanie=opakowanie, ilosc_opakowan = kwargs['ilosc'] )

                if opakowanie_apteki.ilosc < int(kwargs['ilosc']):
                    raise Exception('There is not enough product in selected pharmacy!')
                koszyk.save()
            return 0
