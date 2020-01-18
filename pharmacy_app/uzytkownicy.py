from pprint import pprint

from django.core.management import call_command
from django.db import transaction

from clients.models import Klient, hash_password
from pharmacy_app.models import Pracownik


def dodaj_klienta(**kwargs):
    with transaction.atomic():
        _log_u = Klient.objects.filter(login=kwargs['login'])
        _mail_u = Klient.objects.filter(email=kwargs['email'])
        if _log_u or _mail_u:
            raise Exception('login or mail already used')
        _klient = Klient(
            imie=kwargs['imie'],
            nazwisko=kwargs['nazwisko'],
            adres=kwargs['adres'],
            kod_pocztowy=kwargs['kod_pocztowy'],
            email=kwargs['email'],
            login=kwargs['login'])
        # _klient.add(data_urodzenioa=kwargs['-d'])
        hash_password(client=_klient, password=kwargs['haslo'])
        print(kwargs['haslo'])
        pprint(vars(_klient))
        _klient.save()


def dodaj_aptekarza(**kwargs):
    with transaction.atomic():
        _login = kwargs['admin_login']
        _token = kwargs['admin_token']
        try:
            call_command('autoryzacja_pracownik', _login, _token)
        except:
            raise Exception('Authorization error!')
        try:
            _passwd = kwargs['pass_h']
            _pracownik = Pracownik(login=kwargs[login_h], poziom_dostepu=int(kwargs[level_h]))
            hash_password_(_pracownik, passwd)
        except:
            raise Exception('new user except')
        return 0






