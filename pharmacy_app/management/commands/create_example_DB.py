from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from datetime import datetime
from clients.models import Klient
from pharmacy_app.models import Lek
from pharmacy_app.models import Pracownik
from pharmacy_app.models import Apteka



class Command(BaseCommand):
    help = 'create example'
    def handle(self, *args, **kwargs):
        try:
            _a = Apteka.object.get(nazwa='apt')
        except:
            _apteka = Apteka(nazwa='apt', adres='S7', kod_pocztowy='63-800')
            _apteka.save()
        ###
        try:
            _p = Pracownik.objects.get(login='w1')
        except:
     #       _hash_pracownik
            _pracownik = Pracownik(hash_hasla='hashh', sol_hasla= login='w1', poziom_dostepu=1)
            _pracownik.save()
            _pracownik.apteki.add(_apteka)
            _pracownik.save()
        try:
            _k=Klient.objects.get(login='J_K_S6')
        except:
            _user= Klient(imie='Jan', nazwisko='Kowalski', adres='S6', kod_pocztowy='45-789', email='Jan@Kowalski.com', data_urodzenia=datetime.now(), login='J_K_S6', hash_hasla='passwd123')
            _user.save()
        ###
