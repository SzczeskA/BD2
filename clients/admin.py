from django.contrib import admin

from .models import Klient
from .models import Zamowienie
from .models import Koszyk
from .models import Zgloszenie
from .models import LogAutoryzacja

admin.site.register(Klient)
admin.site.register(Zamowienie)
admin.site.register(Koszyk)
admin.site.register(Zgloszenie)
admin.site.register(LogAutoryzacja)
