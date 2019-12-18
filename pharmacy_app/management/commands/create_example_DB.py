from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.utils import timezone
from datetime import datetime
from io import StringIO
from clients.models import Klient
from pharmacy_app.models import Lek
from pharmacy_app.models import Pracownik
from pharmacy_app.models import Apteka
from pharmacy_app.models import SubstancjaCzynna
from polls.management.commands.logowanie import hash_password_p
from polls.management.commands.logowanie import hash_password


class Command(BaseCommand):
    help = 'create example'
    def handle(self, *args, **kwargs):
        _token = StringIO()
        try:
            _a = Apteka.object.get(nazwa='apt')
        except:
            _apteka = Apteka(nazwa = 'apt', adres = 'S7', kod_pocztowy = '63-800')
            _apteka.save()
        try:
            _p = Pracownik.objects.get(login = 'w1')
        except:
            _pracownik =Pracownik( login = 'w1', poziom_dostepu = 1)
            _pracownik.save()
            hash_password_p(_pracownik, 'hashh_haslo1234')
            _pracownik.apteki.add(_apteka)
            _pracownik.save()
        try:
            _k=Klient.objects.get(login='J_K_S6')
        except:
            _user = Klient(imie='Jan', nazwisko='Kowalski', adres='S6', kod_pocztowy='45-789', email='Jan@Kowalski.com', data_urodzenia=datetime.now(), login='J_K_S6')
            _user.save()
            hash_password(_user, 'hashh_haslo')
        try:
            _A2=Apteka.objects.get(nazwa='apt2')
        except:
            call_command('zaloguj_aptekarz', 'w1', 'hashh_haslo1234', stdout= _token)
            call_command('dodaj_apteke', 'w1', _token.getvalue()[:-1], 'apt2', 'Wroclaw', '34-878' )
        try:
            _p = Klient.objects.get(login='P_Z_S6')
        except:
            call_command('dodaj_klienta', 'Paweł', 'z', 'S6', '45-789', 'Pawell@z.com', 'P_Z_S6', 'Haslo234')
            #call_command('dodaj_klienta', 'Paweł', 'z', 'S6', '45-789', 'Pawel@z.com', 'P_Z_S6', 'Haslo234')
        try:
            _SC = SubstancjaCzynna.objects.get(nazwa='aqua')
        except:
            _sc = SubstancjaCzynna(nazwa='aqua')
            _sc.save()
        try:
            _l = Lek.objects.get(nazwa='ibuprofen')
        except:
            #_token = StringIO()
            #call_command('zaloguj_aptekarz', 'w1', 'hashh_haslo1234', stdout=_token)
            call_command('dodaj_lek', 'w1', _token.getvalue()[:-1], 'ibuprofen', 'Polska')
        ###
