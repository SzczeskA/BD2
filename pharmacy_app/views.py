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


def index(request):
    return HttpResponse("Pharmacy app")
