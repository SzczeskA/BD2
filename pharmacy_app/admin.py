from django.contrib import admin

from .models import Apteka
from .models import Pracownik
from .models import Pracownik_Apteka

admin.site.register(Apteka)
admin.site.register(Pracownik)
admin.site.register(Pracownik_Apteka)
