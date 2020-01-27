import datetime
from pprint import pprint
from django.db import transaction
from django.db.models import Q
from flask import logging

from clients.models import Klient, hash_password, check_password, check_password_p
from pharmacy_app.management.commands.Token import gen_token
from pharmacy_app.models import Pracownik, LogAutoryzacja, Apteka, Lek, SubstancjaCzynna, Opakowanie




#KLIENT#####################################################################################
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
        if not autoryzacja_pracownik(**kwargs):
            raise Exception('Brak uprawnien')
        delete_login = kwargs['delete_login']
        try:
            klient = Klient.objects.get(login=delete_login)
        except:
            raise Exception('Wrong Login')
        klient.delete()
        return True



#APTEKARZ#####################################################################################
def dodaj_aptekarza(**kwargs):
    with transaction.atomic():
        login = kwargs['login']
        token = kwargs['token']
        if autoryzacja_pracownik(**kwargs):
            #if(pracownicy.objects.get(login = login).poziom_dostepu == 1 :
            passwd = kwargs['new_pass']
            pracownik, created = Pracownik.objects.get_or_create(
                login=kwargs['new_login'],
                poziom_dostepu=int(kwargs['new_level_h']))
            hash_password(pracownik, passwd)
            return created
        raise Exception('Authorization failed')


def usun_aptekarza(**kwargs):
    with transaction.atomic():
        _login = kwargs['login']
        _token = kwargs['token']
        if autoryzacja_pracownik(**kwargs):
            # if(pracownicy.objects.get(login = login).poziom_dostepu == 1 :
            _user = Pracownik.objects.get(login=int(kwargs['remove_user']))
            _user.delete()
            return True
        raise Exception('Authorization failed')


#APTEKA#####################################################################################
def dodaj_apteke(**kwargs):
    with transaction.atomic():
        _login = kwargs['login']
        _token = kwargs['token']
        if autoryzacja_pracownik(**kwargs):
            _apteka = Apteka(
                nazwa=kwargs['nazwa'],
                adres=kwargs['adres'],
                kod_pocztowy=kwargs['kod_pocztowy'])
            _apteka.save()
            return True


def usun_apteke(**kwargs):
    with transaction.atomic():
        _login = kwargs['login']
        _token = kwargs['token']
        if autoryzacja_pracownik(**kwargs):
            _apt = Apteka.objects.get(pk=int(kwargs['remove_pharm']))
            _apt.delete()
            return True

#LEK#####################################################################################
def dodaj_lek(**kwargs):
    with transaction.atomic():
        login = kwargs['login']
        token = kwargs['token']
        if not login or not token:
            raise Exception('kwargs incomplete!!!')
        if not autoryzacja_pracownik(**kwargs):
            return False, 'Brak uprawnień'
        substancja = kwargs['substancja'].strip()
        substancja = SubstancjaCzynna.objects.get_or_create(nazwa=substancja)
        substancja.save()
        print("\nDodano substancje")
        nazwa = kwargs['nazwa'].strip()
        kraj = kwargs['kraj'].strip()
        lek = Lek.objects.get_or_create(nazwa=nazwa, kraj_pochodzenia=kraj)
        lek.save()
        lek.substancje_czynne.add(substancja.pk)
        lek.save()
        print("\nDodano Lek")
        dawka = kwargs['dawka'].strip()
        ilosc = int(kwargs['ilosc'].strip())
        opakowanie, created = Opakowanie.objects.get_or_create(
            ile_dawek=ilosc, jednostka_dawki=dawka, lek=lek)
        opakowanie.save()
        if created:
            return True, 'Utworzono lek'
        return True, 'Lek jest już w bazie!'


def usun_lek(**kwargs):
    with transaction.atomic():
        if autoryzacja_pracownik(**kwargs):
            print("autoryzowano usuwanie leku")
            try:
                print("Lek[" + str(kwargs['lek']) + "]")
                drug = Lek.objects.get(nazwa=kwargs['lek'])
                drug.delete()
            except:
                raise Exception('drug doesnt exist')
            else:
                return True

#SUBSTANCJA#####################################################################################
def dodaj_substancje(**kwargs):
    with transaction.atomic():
        _login = kwargs['login']
        _token = kwargs['token']
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

#LOGOWANIE/AUTORYZACJA#####################################################################################
def zaloguj_aptekarz(**kwargs):
    with transaction.atomic():
        login = kwargs['login']
        haslo = kwargs['haslo']
        try:
            pracownik = Pracownik.objects.get(login=login)
        except:
            print('login: ' + login)
            raise Exception('Wrong Login')
        if check_password_p(pracownik, haslo):
            token = gen_token()
            print('Token generated')
            try:
                log, _ = LogAutoryzacja.objects.get_or_create(login=login)
                log.token = token
                log.data_autoryzacji = datetime.datetime.now()
                log.save()
                print("TOKEN:::: " + token)
                return token
            except:
                print("wrong login")
        else:
            raise Exception('wrong password')


def autoryzacja_pracownik(**kwargs):
    with transaction.atomic():
        login = kwargs['login']
        token = kwargs['token']
        log = LogAutoryzacja.objects.get(login=login, token=token)
        if log:
            log.data_autoryzacji = datetime.datetime.now()
            log.save()
            return True


def zaloguj_klient(**kwargs):
    with transaction.atomic():
        login = kwargs['login']
        haslo = kwargs['haslo']
        try:
            klient = Klient.objects.get(login=login)
        except:
            print("LOGIN")
            return
        if check_password(klient, haslo):
            token = gen_token()
            log, _ = LogAutoryzacja.objects.get_or_create(login=login)
            log.token = token
            log.data_autoryzacji = datetime.datetime.now()
            log.save()
            return token


def autoryzacja_klient(**kwargs):
    with transaction.atomic():
        login = kwargs['login']
        token = kwargs['token']
        log = LogAutoryzacja.objects.get(login=login, token=token)
        if log:
            log.data_autoryzacji = datetime.datetime.now()
            return True


def lista_lekow(**kwargs):
    return Lek.objects(nazwa__contains=kwargs['szukany_lek'])


def lista_substancji(**kwargs):
    return SubstancjaCzynna.objects(
        nazwa__contains=kwargs['szukana_substancja'])


def lista_klientow(**kwargs):
    if not autoryzacja_pracownik(**kwargs):
        raise Exception('Brak uprawnień!')
    print(kwargs)
    amount = int(kwargs['amount'])
    result = []
    if 'phrase' not in kwargs:
        clients = Klient.objects.all()
    else:
        phrase = kwargs['phrase']
        clients = Klient.objects.filter(
            Q(login__contains=phrase) |
            Q(imie__contains=phrase) |
            Q(nazwisko__contains=phrase) |
            Q(email__contains=phrase))
    for client in clients[:amount]:
        result.append({
            'login': client.login,
            'imie': client.imie,
            'nazwisko': client.nazwisko,
            'email': client.email})
    print('result: ' + result[0].get('login'))
    return result


def lista_aptekarzy(**kwargs):
    if not autoryzacja_pracownik(**kwargs):
        raise Exception('Brak uprawnień!')
    print(kwargs)
    amount = int(kwargs['amount'])
    result = []
    if 'phrase' not in kwargs:
        employees = Pracownik.objects.all()
    else:
        phrase = kwargs['phrase']
        employees = Pracownik.objects.filter(Q(login__contains=phrase))
    for employee in employees[:amount]:
        result.append({
            'login': employee.login,
            'poziom_dostepu': employee.poziom_dostepu,
            'apteki': employee.apteki.all()})
        print(employee.apteki)
    print('result: ' + result[0].get('login'))
    return result


def lista_aptek(**kwargs):
    return Apteka.objects(
        nazwa__contains=kwargs['szukana_apteka'])
