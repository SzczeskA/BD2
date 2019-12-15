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
            inicjacja_bazy()
        except Poll.DoesNotExist:
            raise CommandError('Wyjątek w inicjacji_bazy')

        # self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))