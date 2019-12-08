import datetime
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import validate_email


class Klient(models.Model):
    imie = models.CharField(max_length=30, null= False)
    nazwisko = models.CharField(max_length=30, null= False)
    adres = models.CharField(max_length=30, null= False)
    kod_pocztowy = models.CharField(max_length=30, null= False)
    email = models.CharField(max_length=30, default='default@default.com', validators= [validate_email])
    data_urodzenia = models.DateTimeField('Data urodzenia')
    login = models.CharField(max_length=30, null= False)
    hash_hasla = models.CharField(max_length=30, null= False)

class Zamowienie(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    data_zamowienia = models.DateTimeField('Data zamowienia')

class Koszyk(models.Model):
    opakowanie = models.ForeignKey('pharmacy_app.Opakowanie', on_delete=models.CASCADE)
    apteka = models.ForeignKey('pharmacy_app.Apteka', on_delete=models.CASCADE)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    ilosc_opakowan = models.IntegerField(null= False, default= 1)

class Zgloszenie(models.Model):
    opakowanie = models.ForeignKey('pharmacy_app.Opakowanie', on_delete=models.CASCADE)
    apteka = models.ForeignKey('pharmacy_app.Apteka', on_delete=models.CASCADE)
    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.CASCADE)
    ilosc_opakowan = models.IntegerField(null= False, default= 1)
    data_realizacj= models.DateTimeField('Data realizacji', null= False)
