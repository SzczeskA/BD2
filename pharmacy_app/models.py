from django.db import models



class Apteka(models.Model):
    nazwa = models.CharField(max_length=30, null=False)
    adres = models.CharField(max_length=30, null=False)
    kod_pocztowy = models.CharField(max_length=6, null=False)


class Pracownik(models.Model):
    hash_hasla = models.CharField(max_length=30, null=False)
    login = models.CharField(max_length=30, unique= True, null=False)
    poziom_dostepu = models.IntegerField(max_length=2, null=False)
    apteki = models.ManyToManyField(Apteka)


#class PracownikApteka(models.Model):
#    pracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
#    apteka = models.ForeignKey(Apteka, on_delete=models.CASCADE)


class SubstancjaCzynna(models.Model):
    nazwa = models.CharField(max_length=30, null=False)


class Lek(models.Model):
    nazwa = models.CharField(max_length=30, null=False)
    kraj_pochodzenia = models.CharField(max_length=30, null=False)
    substancje_czynne = models.ManyToManyField(SubstancjaCzynna)


#class Sub_czynna_Lek (models.Model):
#    lek = models.ForeignKey(Lek, on_delete=models.CASCADE)
#    substancja_czynna = models.ForeignKey(Sub_czynna, on_delete=models.CASCADE)


class Opakowanie(models.Model):
    ilosc_dawek = models.IntegerField(null=False)
    jednostka_dawki = models.IntegerField(max_length=10, null=False)
    lek = models.ForeignKey(Lek, on_delete=models.CASCADE)
