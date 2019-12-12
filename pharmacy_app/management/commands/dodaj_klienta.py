from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from clients.models import Klient



class Command(BaseCommand):
    help = 'Create  users'

    def add_arguments(self, parser):
        parser.add_argument('user', type=Klient, help='uzytkownik')
        
    def handle(self, *args, **kwargs):
        #_klient=Klient.objects.get(login=kwargs['user'])
        #if _klient.hash_hasla.length() < 8 rise.error("haslo")
        _klient.hash_hasla=_hash(_klient.hash_hasla)
        if(not _klient.save())
        #rise.error("login/mail used")

