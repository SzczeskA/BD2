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
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def przegladanie_aptekarzy(request):
    return render(request, 'app/leki.html')

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def przegladanie_klientow_app(request):
    amount = request.GET.get('amount')
    amount = int(amount)
    phrase = request.GET.get('search_name')
    clients = uzytkownicy.lista_klientow(amount, phrase)
    return Response({
        'status': 'ok',
        'data': clients
    })


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def przegladanie_klientow(request):
    return render(request, 'app/uzytkownicy.html')


@api_view(['GET'])
def dodaj_leki_widok(request):
    print('Dodaj leki widok')
    return render(request, 'app/dodaj-lek.html')


@permission_classes((permissions.AllowAny,))
def dodaj_aptekarza_widok(request):
    return render(request, 'app/dodaj-aptekarza.html')


@permission_classes((permissions.AllowAny,))
def usun_aptekarza_widok(request):
    return render(request, 'app/usun-aptekarza.html')


@permission_classes((permissions.AllowAny,))
def usun_leki_widok(request):
    return render(request, 'app/usun-leki.html')


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def remove_me(request):
    ilosc_s = request.GET.get('ilosc')
    if ilosc_s:
        ilosc = int(ilosc_s)
    else:
        ilosc = 0
    return Response({
        'status': 'ok',
        'data': [
            {'nazwa': f'dupozol {i}' + request.GET.get('nazwa'), 'ilosc': i ** 2}
                for i in range(ilosc)
        ]
    })


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
def lista_lekow(request):
    leki = uzytkownicy.lista_lekow(**request.data)
    return Response({"leki": leki})


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

