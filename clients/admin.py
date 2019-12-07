from django.contrib import admin

from .models import Klient
from .models import Zamowienie

admin.site.register(Klient)
admin.site.register(Zamowienie)
