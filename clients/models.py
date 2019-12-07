import datetime
from django.db import models
from django.utils import timezone

class Klient (models.Model):
    Imie = models.CharField(max_length=30)
    Nazwsiko = models.CharField(max_length=30)
    Adres = models.CharField(max_length=30)
    Kod_pocztowy = models.CharField(max_length=30)
    Data_ur = models.DateTimeField('urodzenia Data')
    LOGIN = models.CharField(max_length=30)
    HASH_hasa = models.CharField(max_length=30)

class Zamowienie (models.Model):
    Klient_ID = models.ForeignKey(Klient, on_delete=models.CASCADE)
    Data_zamowienia= models.DateTimeField('zamowienia data')
