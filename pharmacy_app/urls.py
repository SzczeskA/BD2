import re

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('przegladanie-lekow', views.przegladanie_lekow),
    path('dodaj-leki', views.dodaj_leki_widok),
    path('usun_leki', views.usun_leki_widok),

    path('dupa', views.remove_me),
    path('rejestracja', views.dodaj_klienta),
    path('klienci/dodaj', views.dodaj_klienta),
    path('klienci/usun', views.usun_klienta),
    path('wylogowanie/klient', views.wyloguj_klient),
    path('wylogowanie/pracownik', views.wyloguj_pracownik),
    path('pracownicy/dodaj', views.dodaj_aptekarza),
    path('pracownicy/usun', views.usun_aptekarza),
    path('logowanie/pracownik', views.zaloguj_aptekarz),
    path('logowanie/klient', views.zaloguj_klient),
    path('autoryzacja/klient', views.autoryzacja_klient),
    path('autoryzacja/pracownik', views.autoryzacja_pracownik),
    path('leki', views.lista_lekow),
    path('leki/dodaj', views.dodaj_lek),
    path('leki/usun', views.usun_lek),
    path('substancje/dodaj', views.dodaj_substancje),
    path('substancje/usun', views.usun_substancje),
    path('substancje', views.lista_substancji),
    path('apteki', views.lista_aptek),
    path('apteki/dodaj', views.dodaj_apteke),
    path('apteki/usun', views.usun_apteke)
]


# class LekExtra:
#     def __init__(self):
#         self.recepta,
#         self.nazwa,
#         self.producent,
#         self.substancja,
#         self.postac,
#         self.dawka,
#         self.ilosc,
#         self.odplatnosc,
#         self.cena
#
#
#
#
# def generuj_leki(nazwa_pliku):
#     f = open(nazwa_pliku)
#     text = f.read()
#     parsed = text.split("<tr>")
#     for item in parsed:
#         positions = re.split('[<*>]*', item)
#         .recepta
#         .nazwa
#         .producent
#         .substancja
#         .postac
#         .dawka
#         .ilosc
#         .odplatnosc
#         .cena


