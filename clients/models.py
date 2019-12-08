import datetime
from django.db import models
from django.utils import timezone


class Klient(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    adres = models.CharField(max_length=30)
    kod_pocztowy = models.CharField(max_length=30)
    data_urodzenia = models.DateTimeField('urodzenia Data')
    login = models.CharField(max_length=30)
    hash_hasla = models.CharField(max_length=30)


class Zamowienie(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    data_zamowienia = models.DateTimeField('zamowienia data')
