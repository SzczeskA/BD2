from django.contrib import admin

from .models import Apteka
from .models import Pracownik
from .models import SubstancjaCzynna
from .models import Lek
from .models import Opakowanie
from .models import LogAutoryzacja

admin.site.register(Apteka)
admin.site.register(Pracownik)
admin.site.register(SubstancjaCzynna)
admin.site.register(Lek)
admin.site.register(Opakowanie)
admin.site.register(LogAutoryzacja)
