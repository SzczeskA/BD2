import datetime
from django.db import models
from django.utils import timezone

class Apteka (models.Model):
    Nazwa = models.CharField(max_length=30, null=False)
    Adres = models.CharField(max_length=30, null=False)
    Kod_pocztowy = models.CharField(max_length=6, null=False)

class Pracownik (models.Model):
    HASH_hasla = models.CharField(max_length=30, null=False)
    LOGIN = models.CharField(max_length=30, unique= True, null=False)
    Poziom_dostpu = models.IntegerField(max_length=2, null=False)

class Pracownik_Apteka (models.Model):
    Pracownik_ID = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    Apteka_ID = models.ForeignKey(Apteka, on_delete=models.CASCADE)

class Sub_czynna (models.Model):
    Nazwa = models.CharField(max_length=30, null=False)

class Lek (models.Model):
    Nazwa = models.CharField(max_length=30, null=False)
    Kraj_poch = models.CharField(max_length=30, null=False)

class Sub_czynna_Lek (models.Model):
    Lek_ID = models.ForeignKey(Lek, on_delete=models.CASCADE)
    Sub_ID = models.ForeignKey(Sub_czynna, on_delete=models.CASCADE)

class Opakowanie (models.Model):
    Ile_dawek= models.IntegerField(max_length= 10, null=False)
    Jednostka_dawki= models.IntegerField(max_length= 10, null=False)
    Lek_ID = models.ForeignKey(Lek, on_delete=models.CASCADE)
