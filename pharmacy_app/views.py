from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from sqlalchemy import Integer

from pharmacy_app import uzytkownicy


@permission_classes((permissions.AllowAny,))
def index(request):
    return render(request, 'app/index.html')


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def przegladanie_lekow(request):
    return render(request, 'app/leki.html')


# ograniczenia
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def przegladanie_aptekarzy_app(request):
    print('PRZEGLADANIE APTEKARZY')
    employees = uzytkownicy.lista_aptekarzy(**request.data)
    return Response({
        'status': 'ok',
        'data': employees
    })

# ograniczenia
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def przegladanie_aptekarzy(request):
    return render(request, 'app/aptekarze.html')

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def przegladanie_klientow_app(request):
    clients = uzytkownicy.lista_klientow(**request.data)
    return Response({
        'status': 'ok',
        'data': clients
    })


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def przegladanie_klientow(request):
    return render(request, 'app/uzytkownicy.html')


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def koszyk(request):
    return render(request, 'app/koszyk.html')


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def koszyk_app(request):
    # TUTAJ IMPLEMENTUJ
    clients = uzytkownicy.lista_klientow(**request.data)
    return Response({
        'status': 'ok',
        'data': clients
    })


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def usun_leki_widok(request):
    return render(request, 'app/usun-leki.html')

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def dodaj_leki_widok(request):
    return render(request, 'app/dodaj-lek.html')

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def dodaj_aptekarza_widok(request):
    return render(request, 'app/dodaj-aptekarza.html')

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def usun_aptekarza_widok(request):
    return render(request, 'app/usun-aptekarza.html')

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def dodaj_apteke_widok(request):
    return render(request, 'app/dodaj-apteke.html')

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def usun_apteke_widok(request):
    return render(request, 'app/usun-apteke.html')





@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def dodaj_klienta(request):
    if uzytkownicy.dodaj_klienta(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def usun_klienta(request):
    if uzytkownicy.usun_klienta(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def autoryzacja_klient(request):
    if uzytkownicy.autoryzacja_klient(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def autoryzacja_pracownik(request):
    if uzytkownicy.autoryzacja_pracownik(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def usun_aptekarza(request):
    if uzytkownicy.usun_aptekarza(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST', 'GET'])
@permission_classes((permissions.AllowAny,))
def dodaj_aptekarza(request):
    if uzytkownicy.dodaj_aptekarza(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def dodaj_apteke(request):
    if uzytkownicy.dodaj_apteke(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def usun_apteke(request):
    if uzytkownicy.usun_apteke(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST', 'GET'])
@permission_classes((permissions.AllowAny,))
def dodaj_lek(request):
    print('dodaj lek, data:')
    print(request.data)
    status, alert = uzytkownicy.dodaj_lek(**request.data)
    if status:
        return Response({"status": "ok", 'alert': alert})
    return Response({"status": "error", 'alert': alert})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def usun_lek(request):
    if uzytkownicy.usun_lek(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def dodaj_substancje(request):
    if uzytkownicy.dodaj_substancje(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def usun_substancje(request):
    if uzytkownicy.usun_substancje(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def dodaj_apteke(request):
    if uzytkownicy.dodaj_apteke(**request.data):
        return Response({"status": "ok"})
    return Response({"status": "error"})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def zaloguj_aptekarz(request):
    token = uzytkownicy.zaloguj_aptekarz(**request.data)
    if token:
        return Response({"status": "ok", 'token': token})
    return Response({"status": "error"})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def zaloguj_klient(request):
    token = uzytkownicy.zaloguj_klient(**request.data)
    if token:
        return Response({"status": "ok", "token": token})
    return Response({"status": "error"})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def wyloguj_klient(request):
    #token = uzytkownicy.zaloguj_klient(**request.data)
    #if token:
    return Response({"status": "ok"})
    #return Response({"status": "error"})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def wyloguj_pracownik(request):
    #token = uzytkownicy.zaloguj_klient(**request.data)
    #if token:
    print("LOGOUT")
    return Response({"status": "ok"})
    #return Response({"status": "error"})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def lista_lekow_app(request):
    leki = uzytkownicy.lista_lekow(**request.data)
    return Response({"leki": leki})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def lista_lekow(request):
    return render(request, 'app/leki')


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def lista_substancji(request):
    substancje = uzytkownicy.lista_substancji(**request.data)
    return Response({"substancje": substancje})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def lista_aptek(request):
    apteki = uzytkownicy.lista_aptek(**request.data)
    return Response({"apteki": apteki})

