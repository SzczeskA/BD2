import hashlib
import os

from django.db import models, transaction
from django.core.validators import validate_email


class Klient(models.Model):
    imie = models.CharField(max_length=30, null=False)
    nazwisko = models.CharField(max_length=30, null=False)
    adres = models.CharField(max_length=30, null=False)
    kod_pocztowy = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=30, default='default@default.com', validators=[validate_email])
    data_urodzenia = models.DateTimeField('Data urodzenia', null=True)
    login = models.CharField(max_length=30, null=False)
    hash_hasla = models.BinaryField(max_length=128, null=False)
    sol_hasla = models.BinaryField(max_length=32, null=False)
    def __str__(self):
        return self.imie + self.nazwisko + self.login


class Zamowienie(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    data_zamowienia = models.DateTimeField('Data zamowienia', auto_now=True)


class Koszyk(models.Model):
    opakowanie = models.ForeignKey('pharmacy_app.Opakowanie', on_delete=models.CASCADE)
    apteka = models.ForeignKey('pharmacy_app.Apteka', on_delete=models.CASCADE)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    ilosc_opakowan = models.IntegerField(null=False, default=1)


class Zgloszenie(models.Model):
    opakowanie = models.ForeignKey('pharmacy_app.Opakowanie', on_delete=models.CASCADE)
    apteka = models.ForeignKey('pharmacy_app.Apteka', on_delete=models.CASCADE)
    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.CASCADE)
    ilosc_opakowan = models.IntegerField(null=False, default=1)
    data_realizacj= models.DateTimeField('Data realizacji', null=False, auto_now=True)


class LogAutoryzacja(models.Model):
    token = models.CharField( max_length=30, null=False, default='')
    login = models.CharField(max_length=30, unique=True, null=False)
    data_autoryzacji= models.DateTimeField('Czas ostatniej autoryzacji', null=True)
    #pracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE)


class ZamowienieError:
    def __init__(self, wartosc):
        self.wartosc = wartosc

    def __str__(self):
        return self.wartosc


@transaction.atomic
def hash_password(client, password):
    max_len = 1000

    if len(password) > max_len:
        raise Exception('Password should be shorter than 1000 chars.')
    salt = os.urandom(32)  # Remember this

    key = get_hash(salt, password)
    client.hash_hasla = key
    client.sol_hasla = salt
    client.save()


def get_hash(salt, password):
    return hashlib.pbkdf2_hmac(
        'sha256',  # The hash digest algorithm for HMAC
        password.encode('utf-8'),  # Convert the password to bytes
        salt,  # Provide the salt
        100000,  # It is recommended to use at least 100,000 iterations of SHA-256
        dklen=128  # Get a 128 byte key
    )


def check_password(client, password):
    return bytes(client.hash_hasla) == get_hash(client.sol_hasla, password)


@transaction.atomic
def hash_password_p(pracownik, password):
    max_len = 1000

    if len(password) > max_len:
        raise Exception('Password should be shorter than 1000 chars.')
    salt = os.urandom(32)  # Remember this

    key = get_hash(salt, password)
    pracownik.hash_hasla = key
    pracownik.sol_hasla = salt
    pracownik.save()


def check_password_p(pracownik, password):
    return bytes(pracownik.hash_hasla) == get_hash(pracownik.sol_hasla, password)








