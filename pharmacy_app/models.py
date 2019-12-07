import datetime
from django.db import models
from django.utils import timezone

class Apteka (models.Model):
    Nazwa = models.CharField(max_length=30)
    Adres = models.CharField(max_length=30)
    Kod_pocztowy = models.CharField(max_length=6)

class Pracownik (models.Model):
    HASH_hasla = models.CharField(max_length=30)
    LOGIN = models.CharField(max_length=30, unique= True)
    Poziom_dostpu = models.IntegerField(max_length=2)

class Pracownik_Apteka (models.Model):
    Pracownik_ID = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    Apteka_ID = models.ForeignKey(Apteka, on_delete=models.CASCADE)
