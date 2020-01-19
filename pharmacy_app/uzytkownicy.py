import datetime
#from StringIO import StringIO
from pprint import pprint

from django.core.management import call_command
from django.db import transaction

from clients.models import Klient, hash_password, check_password, check_password_p
from pharmacy_app.management.commands.Token import genToken
from pharmacy_app.models import Pracownik, LogAutoryzacja, Apteka, Lek, SubstancjaCzynna


def autoryzacja_klient(**kwargs):
    with transaction.atomic():
        _login = kwargs['user_login']
        _token = kwargs['user_token']
        _log = LogAutoryzacja.objects.get(login=_login)
        _time = _log.data_autoryzacji + datetime.timedelta(minutes=15)
        _now = datetime.now()
        if _log.token == _token:  # and _time > _now:
            # _log.data_autoryzacji = datetime.now()  ##timezone
            # _log.update(data_autoryzacji = datetime.now())
            print('aut')
        else:
            raise Exception('nieautoryzowany dostep')


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


def autoryzacja_pracownik(**kwargs):
    with transaction.atomic():
        _login = kwargs['admin_login']
        _token = kwargs['admin_token']
        _log = LogAutoryzacja.objects.get(login=_login)
        _time = _log.data_autoryzacji + datetime.timedelta(minutes=15)
        _now = datetime.datetime.now()
        if _log.token == _token:  # and _time > _now:
            # _log.data_autoryzacji = datetime.now()  ##timezone
            # _log.update(data_autoryzacji = datetime.now())
            print('autoryzowano', _login)
            return True


def dodaj_aptekarza(**kwargs):
    with transaction.atomic():
        _login = kwargs['admin_login']
        _token = kwargs['admin_token']
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
        #out = StringIO()
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
        _login = kwargs['admin_login']
        _token = kwargs['admin_token']
        if autoryzacja_pracownik(**kwargs):
            _lek = Lek(
                nazwa=kwargs['drug_name'],
                kraj_pochodzenia=kwargs['drug_country'])
            # kwargs['drug_activeSub'])
            _lek.save()
            # _lek.add(substancje_czynne= int(kwargs['drug_activeSub']))
            # _lek.save()
            return True


def usun_lek(**kwargs):
    with transaction.atomic():
        _login = kwargs['admin_login']
        _token = kwargs['admin_token']
        if autoryzacja_pracownik(**kwargs):
            try:
                _drug = Lek.objects.get(pk=int(kwargs['remove_drug']))
                _drug.delete()
            except:
                raise Exception('drug doesnt exist')
            else:
                return True
        return 0


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
            try:
                _ulog = LogAutoryzacja.objects.get(login=_login)
                _ulog.token = _token
                _ulog.update()
                return _token
            except:
                _log = LogAutoryzacja(
                    login=_login,
                    token=_token,
                    data_autoryzacji=datetime.now())
                _log.save()
                return _token
        else:
            raise Exception('wrong password')


def zaloguj_klient(**kwargs):
    with transaction.atomic():
        _login = kwargs['login']
        _haslo = kwargs['haslo']
        try:
            _klient = Klient.objects.get(login=_login)
        except:
            raise Exception('Wrong Login')
        if check_password(_klient, _haslo):
            _token = genToken()
            try:
                _ulog = LogAutoryzacja.objects.get(login=_login)
                _ulog.token = _token
                _ulog.update()
                return _token
            except:
                _log = LogAutoryzacja(
                    login=_login,
                    token=_token,
                    data_autoryzacji=datetime.now())
                _log.save()
                return _token
        else:
            raise Exception('wrong password')


def lista_lek(**kwargs):
    return Lek.objects(nazwa__contains=kwargs['szukany_lek'])


def lista_substancja_czynna(**kwargs):
    return SubstancjaCzynna.objects(
        nazwa__contains=kwargs['szukana_substancja'])


