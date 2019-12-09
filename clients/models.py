from django.db import models
from django.core.validators import validate_email
from django.db import transaction

from BD2.pharmacy_app.models import OpakowaniaApteki


class Klient(models.Model):
    imie = models.CharField(max_length=30, null=False)
    nazwisko = models.CharField(max_length=30, null=False)
    adres = models.CharField(max_length=30, null=False)
    kod_pocztowy = models.CharField(max_length=30, null= False)
    email = models.CharField(max_length=30, default='default@default.com', validators= [validate_email])
    data_urodzenia = models.DateTimeField('Data urodzenia')
    login = models.CharField(max_length=30, null=False)
    hash_hasla = models.CharField(max_length=30, null=False)

class Zamowienie(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    data_zamowienia = models.DateTimeField('Data zamowienia')

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
    data_realizacj= models.DateTimeField('Data realizacji', null=False)


class ZamowienieError:
    def __init__(self, wartosc):
        self.wartosc = wartosc

    def __str__(self):
        return self.wartosc


@transaction.atomic
def wykonaj_zamowienie(zamowienie):
    klient = Klient.objects.get(pk=zamowienie.klient.pk)
    koszyki = Koszyk.objects.filter(klient=klient)
    for koszyk in koszyki:
        opakowania_apteki = OpakowaniaApteki.object.get(opakowanie=koszyk.opakowanie, apteka=koszyk.apteka)
        if opakowania_apteki.ilosc < koszyk.ilosc_opakowan:
            raise ZamowienieError('Brak produktu' + opakowania_apteki.opakowanie)
        opakowania_apteki.ilosc -= koszyk.ilosc_opakowan
        opakowania_apteki.save()

#def inicjacja_bazy():
#    klient = Klient
#    klient.adres = 'Losowy adres 11, Wrocław'





