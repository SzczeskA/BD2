import datetime
from pprint import pprint
from django.db import transaction
from flask import logging

from clients.models import Klient, hash_password, check_password, check_password_p
from pharmacy_app.management.commands.Token import genToken
from pharmacy_app.models import Pracownik, LogAutoryzacja, Apteka, Lek, SubstancjaCzynna, Opakowanie





def dodaj_klienta(**kwargs):
    with transaction.atomic():
        _log_u = Klient.objects.filter(login=kwargs['login'])
        _mail_u = Klient.objects.filter(email=kwargs['email'])
        if _log_u or _mail_u:
            raise Exception('login or mail already used')
        _klient = Klient(
            imie='xx',       #kwargs['imie'],
            nazwisko='x',   #kwargs['nazwisko'],
            adres='x',      #kwargs['adres'],
            kod_pocztowy='22-222',  #kwargs['kod_pocztowy'],
            email=kwargs['email'],
            login=kwargs['login'])
        # _klient.add(data_urodzenioa=kwargs['-d'])
        hash_password(client=_klient, password=kwargs['haslo'])
        print(kwargs['haslo'])
        pprint(vars(_klient))
        _klient.save()


#wydaje mi sie, ze powinno byc raczej potwierdzanie sesji tutaj...
#no i moze nie sam klient siebie, ale pracownik klienta?

def usun_klienta(**kwargs):
    with transaction.atomic():
        _login = kwargs['login']
        _hash = kwargs['haslo']
        try:
            _klient = Klient.objects.get(login=_login)
        except:
            raise Exception('Wrong Login')
        if check_password(_klient, _hash):
            _klient.delete()
            return True;




def dodaj_aptekarza(**kwargs):
    with transaction.atomic():
        _login = kwargs['user_login']
        _token = kwargs['user_token']
        if autoryzacja_pracownik(**kwargs):
            _passwd = kwargs['pass_h']
            _pracownik, created = Pracownik.objects.get_or_create(
                login=kwargs['login_h'],
                poziom_dostepu=int(kwargs['level_h']))
            hash_password(_pracownik, _passwd)
            return created


def usun_aptekarza(**kwargs):
    with transaction.atomic():
        _login = kwargs['admin_login']
        _token = kwargs['admin_token']
        if autoryzacja_pracownik(**kwargs):
            try:
                _user = Pracownik.objects.get(login=int(kwargs['remove_user']))
                _user.delete()
                return True
            except:
                return False


def dodaj_apteke(**kwargs):
    with transaction.atomic():
        _login = kwargs['admin_login']
        _token = kwargs['admin_token']
        if autoryzacja_pracownik(**kwargs):
            _apteka = Apteka(
                nazwa=kwargs['nazwa'],
                adres=kwargs['adres'],
                kod_pocztowy=kwargs['kod_pocztowy'])
            _apteka.save()
            return True


def usun_apteke(**kwargs):
    with transaction.atomic():
        _login = kwargs['admin_login']
        _token = kwargs['admin_token']
        if autoryzacja_pracownik(**kwargs):
            _apt = Apteka.objects.get(pk=int(kwargs['remove_pharm']))
            _apt.delete()
            return True


def dodaj_lek(**kwargs):
    with transaction.atomic():
        login = kwargs['admin_login']
        token = kwargs['admin_token']
        if not autoryzacja_pracownik(**kwargs):
            return False
        substancja = kwargs['substancja'].strip()
        substancja = SubstancjaCzynna.objects.get_or_create(nazwa=substancja)
        substancja.save()
        nazwa = kwargs['nazwa'].strip()
        kraj = kwargs['kraj'].strip()
        lek = Lek.objects.get_or_create(nazwa=nazwa, kraj=kraj, substancje_czynne=substancja)
        lek.save()
        dawka = kwargs['dawka'].strip()
        ilosc = int(kwargs['ilosc'].strip())
        opakowanie = Opakowanie.objects.get_or_create(
            ile_dawek=ilosc, jednostka_dawki=dawka, lek=lek)
        opakowanie.save()
        return True


def usun_lek(**kwargs):
    with transaction.atomic():
        #_login = kwargs['user_login']
        #_token = kwargs['user_token']
        if autoryzacja_pracownik(**kwargs):
            print("autoryzowano usuwanie leku")
            try:
                print("Lek["+ str(kwargs['lek']) + "]")
                _drug = Lek.objects.get(nazwa=kwargs['lek'])
                _drug.delete()
            except:
                raise Exception('drug doesnt exist')
            else:
                return True


def dodaj_substancje(**kwargs):
    with transaction.atomic():
        _login = kwargs['admin_login']
        _token = kwargs['admin_token']
        if autoryzacja_pracownik(**kwargs):
            substancja = SubstancjaCzynna(nazwa=kwargs['nazwa_substancji'])
            substancja.save()
            return True

def usun_substancje(**kwargs):
    with transaction.atomic():
        _login = kwargs['admin_login']
        _token = kwargs['admin_token']
        if autoryzacja_pracownik(**kwargs):
            try:
                substancja = SubstancjaCzynna.objects.get(
                    pk=int(kwargs['id_substancji']))
                substancja.delete()
            except:
                raise Exception('drug doesnt exist')
            else:
                return True


def zaloguj_aptekarz(**kwargs):
    with transaction.atomic():
        _login = kwargs['login']
        _haslo = kwargs['haslo']
        try:
            _pracownik = Pracownik.objects.get(login=_login)
        except:
            raise Exception('Wrong Login')
        if check_password_p(_pracownik, _haslo):
            _token = genToken()
            print('OK print')
            try:
                _ulog, created = LogAutoryzacja.objects.get_or_create(login=_login)
                if created:
                    _ulog.token = _token
                    try:
                        _ulog.update()
                    except:
                        _ulog.save()
                print ("TOKEN:::: "+_token)
                return _token
            except:
                print("wrong login")
        else:
            raise Exception('wrong password')


def autoryzacja_pracownik(**kwargs):
    with transaction.atomic():
        login = kwargs['user_login']
        token = kwargs['user_token']
        print(':::::::Autoryzacja:' + login + 'z tokenem ' + token)
        log = LogAutoryzacja.objects.get(login=login)
        if log:
            print('Autoryzowano', login)
            return True
        raise('Brak poprawnego tokenu')
        return False


def zaloguj_klient(**kwargs):
    with transaction.atomic():
        _login = kwargs['login']
        _haslo = kwargs['haslo']
        try:
            _klient = Klient.objects.get(login=_login)
        except:
            print("LOGIN")
            return
        if check_password(_klient, _haslo):
            _token = genToken()
            _ulog, created = LogAutoryzacja.objects.get_or_create(login=_login)
            if created:
                _ulog.token = _token
                try:
                   _ulog.update()
                except:
                   _ulog.save()
            return _token



def autoryzacja_klient(**kwargs):
    with transaction.atomic():
        _login = kwargs['user_login']
        _token = kwargs['user_token']
        _log = LogAutoryzacja.objects.get(login=_login)
        #_time = _log.data_autoryzacji + datetime.timedelta(minutes=15)
        _now = datetime.datetime.now()
        if _log.token == _token:  # and _time > _now:
            #_log.data_autoryzacji = datetime.now()  ##timezone
            _log.update(data_autoryzacji=datetime.datetime.now())
            print('aut')
            return True

def lista_lekow(**kwargs):
    return Lek.objects(nazwa__contains=kwargs['szukany_lek'])


def lista_substancji(**kwargs):
    return SubstancjaCzynna.objects(
        nazwa__contains=kwargs['szukana_substancja'])


def lista_aptek(**kwargs):
    return Apteka.objects(
        nazwa__contains=kwargs['szukana_apteka'])
