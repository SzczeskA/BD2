from django.db import models


class Apteka(models.Model):
    nazwa = models.CharField(max_length=30, null=False, unique= True)
    adres = models.CharField(max_length=30, null=False)
    kod_pocztowy = models.CharField(max_length=6, null=False)


class Pracownik(models.Model):
    hash_hasla = models.BinaryField(max_length=128, null=False)
    sol_hasla = models.BinaryField(max_length=32, null=False)
    login = models.CharField(max_length=30, unique=True, null=False)
    # poziom_dostepu
    poziom_dostepu = models.IntegerField(null=False, default=0)
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


class OpakowaniaApteki(models.Model):
    opakowanie = models.ForeignKey(
        Opakowanie,
        null=False,
        on_delete=models.CASCADE)
    ilosc = models.IntegerField()
    apteka = models.ForeignKey(Apteka, on_delete=models.CASCADE)


class LogAutoryzacja(models.Model):
    token = models.CharField(max_length=30, null=False, default='')
    login = models.CharField(max_length=30, unique=True, null=False)
    data_autoryzacji= models.DateTimeField(
        'Czas ostatniej autoryzacji',
        null=True)
    #pracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE)

