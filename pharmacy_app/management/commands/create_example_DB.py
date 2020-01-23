from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.utils import timezone
from datetime import datetime
from io import StringIO
from clients.models import Klient
from pharmacy_app.models import Lek, Opakowanie, OpakowaniaApteki
from pharmacy_app.models import Pracownik
from pharmacy_app.models import Apteka
from pharmacy_app.models import SubstancjaCzynna
from polls.management.commands.logowanie import hash_password_p
from polls.management.commands.logowanie import hash_password


class Command(BaseCommand):
    aptekarz = Pracownik(login='admin', poziom_dostepu=1)
    hash_password_p(pracownik=aptekarz, password='admin')
    aptekarz.apteki.add(Apteka.objects.get(nazwa='apt'))
    aptekarz.save()



def inny_kod():
    help = 'create example'
    def handle(self, *args, **kwargs):
        _token = StringIO()
        _token_k = StringIO()
        try:
            _a = Apteka.object.get(nazwa='apt')
        except:
            _apteka = Apteka(nazwa = 'apt', adres = 'sdasd', kod_pocztowy = '63-800')
            _apteka.save()
        try:
            _p = Pracownik.objects.get(login = 'admin')
        except:
            _pracownik =Pracownik( login = 'admin', poziom_dostepu = 1)
            _pracownik.save()
            hash_password_p(_pracownik, 'admin')
            _pracownik.apteki.add(_apteka)
            _pracownik.save()
        return
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
            call_command('zaloguj_klient', 'P_Z_S6', 'Haslo234', stdout=_token_k)
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
        try:
            _op = Opakowanie.objects.get(lek=Lek.objects.get(nazwa='ibuprofen'))
        except:
            _op = Opakowanie(ile_dawek=1, jednostka_dawki=1, lek=Lek.objects.get(nazwa='ibuprofen'))
            _op.save()
            try:
                call_command('dodaj_do_koszyka', 'P_Z_S6', _token_k.getvalue()[:-1], str(_op.pk), str(_apteka.pk), str(1))
            except:
                print('brak opakowan')
            _opa= OpakowaniaApteki(opakowanie=_op, ilosc= 15, apteka=_apteka)
            _opa.save()
            call_command('dodaj_do_koszyka', 'P_Z_S6', _token_k.getvalue()[:-1], str(_op.pk), str(_apteka.pk), str(1))
        ###
