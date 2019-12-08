from django.contrib import admin

from .models import Apteka
from .models import Pracownik
from .models import Pracownik_Apteka
from .models import Sub_czynna
from .models import Lek
from .models import Sub_czynna_Lek
from .models import Opakowanie

admin.site.register(Apteka)
admin.site.register(Pracownik)
admin.site.register(Pracownik_Apteka)
admin.site.register(Sub_czynna)
admin.site.register(Lek)
admin.site.register(Sub_czynna_Lek)
admin.site.register(Opakowanie)
