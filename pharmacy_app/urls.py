from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello_world, name='hello_world'),
    path('klient/dodaj', views.dodaj_klienta),
    path('klient/usun', views.usun_klienta)
]
