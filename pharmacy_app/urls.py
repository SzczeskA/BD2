import re
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('przegladanie-lekow', views.przegladanie_lekow),
    path('uzytkownicy', views.przegladanie_klientow),
    path('aptekarze', views.przegladanie_aptekarzy),

    path('uzytkownicy-app', views.przegladanie_klientow_app),
    path('aptekarze-app', views.przegladanie_aptekarzy_app),
    path('uzytkownicy-app/usun', views.usun_klienta),
    path('aptekarze-app/usun', views.usun_aptekarza),
    path('koszyk', views.koszyk),
    path('koszyk-app', views.koszyk_app),

    #path('app-dodaj-lek', views.dodaj_leki_widok),
    path('dodaj-leki', views.dodaj_leki_widok),
    path('usun-leki', views.usun_leki_widok),
    path('usun-aptekarza', views.usun_aptekarza_widok),
    path('dodaj-aptekarza', views.dodaj_aptekarza_widok),
    path('usun-apteke', views.usun_apteke_widok),
    path('dodaj-apteke', views.dodaj_aptekarza_widok),


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
    path('leki-app', views.lista_lekow),
    path('leki/dodaj', views.dodaj_leki_widok),
    path('leki/usun', views.usun_lek),
    path('substancje/dodaj', views.dodaj_substancje),
    path('substancje/usun', views.usun_substancje),
    path('substancje', views.lista_substancji),
    path('apteki', views.lista_aptek),
    path('apteki/dodaj', views.dodaj_apteke),
    path('apteki/usun', views.usun_apteke)
]



