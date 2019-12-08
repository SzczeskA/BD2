from django.db import models


class Apteka(models.Model):
    nazwa = models.CharField(max_length=30, null=False)
    adres = models.CharField(max_length=30, null=False)
    kod_pocztowy = models.CharField(max_length=6, null=False)

class Pracownik(models.Model):
    hash_hasla = models.CharField(max_length=30, null=False)
    login = models.CharField(max_length=30, unique=True, null=False)
    poziom_dostepu = models.IntegerField(null=False)
    apteki = models.ManyToManyField(Apteka)

class SubstancjaCzynna(models.Model):
    nazwa = models.CharField(max_length=30, null=False)

class Lek(models.Model):
    nazwa = models.CharField(max_length=30, null=False)
    kraj_pochodzenia = models.CharField(max_length=30, null=False)
    substancje_czynne = models.ManyToManyField(SubstancjaCzynna)

class Opakowanie(models.Model):
    ile_dawek = models.IntegerField(null=False)
    jednostka_dawki = models.IntegerField(null=False)
    lek = models.ForeignKey(Lek, on_delete=models.CASCADE)
