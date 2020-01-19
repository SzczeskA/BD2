from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pharmacy_app import uzytkownicy


@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})


@api_view(['POST'])
def dodaj_klienta(request):
    if uzytkownicy.dodaj_klienta(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
def usun_klienta(request):
    if uzytkownicy.usun_klienta(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
def autoryzacja_klient(request):
    if uzytkownicy.autoryzacja_klient(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
def autoryzacja_pracownik(request):
    if uzytkownicy.autoryzacja_pracownik(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
def usun_aptekarza(request):
    if uzytkownicy.usun_aptekarza(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
def dodaj_aptekarza(request):
    if uzytkownicy.dodaj_aptekarza(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
def dodaj_apteke(request):
    if uzytkownicy.dodaj_apteke(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
def usun_apteke(request):
    if uzytkownicy.usun_apteke(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
def dodaj_lek(request):
    if uzytkownicy.dodaj_lek(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
def usun_lek(request):
    if uzytkownicy.usun_lek(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
def dodaj_apteke(request):
    if uzytkownicy.dodaj_apteke(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
def zaloguj_aptekarz(request):
    if uzytkownicy.zaloguj_aptekarz(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
def zaloguj_klient(request):
    if uzytkownicy.zaloguj_klient(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
def lista_lekow(request):
    leki = uzytkownicy.lista_lekow(**request.data)
    return Response({"leki": leki})


@api_view(['POST'])
def lista_substancji(request):
    substancje = uzytkownicy.lista_substancji(**request.data)
    return Response({"substancje": substancje})


@api_view(['POST'])
def lista_aptek(request):
    apteki = uzytkownicy.lista_aptek(**request.data)
    return Response({"apteki": apteki})


def index(request):
    return HttpResponse("Pharmacy app")
