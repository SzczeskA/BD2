from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from datetime import datetime
from clients.models import Klient
from clients.models import LogAutoryzacja as client_log
from pharmacy_app.models import LogAutoryzacja as pharm_log
from pharmacy_app.models import Lek
from pharmacy_app.models import Pracownik
from pharmacy_app.models import Apteka



class Command(BaseCommand):
    help = 'create example'

    def handle(self, *args, **kwargs):
        ##
        try:
            _user= Klient.objects.get(login='J_K_S6')
            _user.delete()
        except:
            print('user error')

        try:
            _pracownik= Pracownik.objects.get(login='w1')
            _pracownik.delete()
        except:
            print('worker error')

        try:
            _apteka= Apteka.objects.get(nazwa='apt')
            _apteka.delete() 
        except:
            print('apt error')

        ##
