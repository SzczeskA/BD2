from django.db import models
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
    data_realizacj = models.DateTimeField('Data realizacji', null=False, auto_now=True)


class ZamowienieError:
    def __init__(self, wartosc):
        self.wartosc = wartosc

    def __str__(self):
        return self.wartosc







