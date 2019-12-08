import datetime
from django.db import models
from django.utils import timezone

class Apteka (models.Model):
    nazwa = models.CharField(max_length=30, null=False)
    adres = models.CharField(max_length=30, null=False)
    kod_pocztowy = models.CharField(max_length=6, null=False)

class Pracownik (models.Model):
    hash_hasla = models.CharField(max_length=30, null=False)
    login = models.CharField(max_length=30, unique= True, null=False)
    poziom_dostpu = models.IntegerField(max_length=2, null=False)
    apteki = models.ManyToManyField(Apteka)

class SubstancjaCzynna (models.Model):
    nazwa = models.CharField(max_length=30, null=False)

class Lek (models.Model):
    nazwa = models.CharField(max_length=30, null=False)
    kraj_poch = models.CharField(max_length=30, null=False)
    substancje_czynne = models.ManyToManyField(SubstancjaCzynna)

class Opakowanie (models.Model):
    ile_dawek= models.IntegerField(max_length= 10, null=False)
    jednostka_dawki= models.IntegerField(max_length= 10, null=False)
    lek = models.ForeignKey(Lek, on_delete=models.CASCADE)
