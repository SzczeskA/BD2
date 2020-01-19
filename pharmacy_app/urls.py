from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello_world, name='hello_world'),
    path('rejestracja', views.dodaj_klienta),
    path('klienci/dodaj', views.dodaj_klienta),
    path('klienci/usun', views.usun_klienta),
    path('logowanie/klient', views.zaloguj_klient),
    path('pracownicy/dodaj', views.dodaj_aptekarza),
    path('pracownicy/usun', views.usun_aptekarza),
    path('logowanie/pracownik', views.zaloguj_aptekarz),
    path('leki', views.lista_lekow),
    path('substancje', views.lista_substancji),
    path('apteki', views.lista_aptek),
]
