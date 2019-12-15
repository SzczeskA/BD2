from django.core.management.base import BaseCommand, CommandError

from clients.models import Koszyk, Zamowienie, Klient
from pharmacy_app.models import OpakowaniaApteki, Opakowanie, Apteka, Lek
from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        try:
            inicjalizacja_bazy()
        except Poll.DoesNotExist:
            raise CommandError('Wyjątek w inicjacji_bazy')

        # self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))

def inicjalizacja_bazy():
    klient = Klient(adres='Losowy adres 11, Wrocław', imie='Andrzej', nazwisko='Kowal', kod_pocztowy='77-534',
                    login='akowal', hash_hasla='sfkhsdf')
    klient.save()
    zamowienie = Zamowienie(klient=klient)
    zamowienie.save()
    lek = Lek(nazwa='Ibuprom')
    lek.save()
    apteka = Apteka(nazwa='Ziko', adres='Krakowska 14', kod_pocztowy='85-999')
    apteka.save()
    opakowanie = Opakowanie(lek=lek, ile_dawek=50, jednostka_dawki=200)
    opakowanie.save()
    opakowanie_apteki = OpakowaniaApteki(opakowanie=opakowanie, ilosc=30, apteka=apteka)
    opakowanie_apteki.save()
    koszyk = Koszyk(opakowanie=opakowanie, klient=klient, apteka=apteka, ilosc_opakowan=2)
    koszyk.save()


