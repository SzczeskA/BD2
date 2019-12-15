import hashlib
import os

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from clients.models import Klient
from polls.models import Question as Poll


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('password', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            password = options['password'][0]
            hash_password(client=Klient.objects.get(pk=3), password=password)
        except Poll.DoesNotExist:
            raise CommandError('Wyjątek w inicjalizacji_bazy')

        # self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))


@transaction.atomic
def hash_password(client, password):
    max_len = 1000

    if len(password) > max_len:
        raise Exception('Password should be shorter than 1000 chars.')
    salt = os.urandom(32)  # Remember this

    key = hashlib.pbkdf2_hmac(
        'sha256',  # The hash digest algorithm for HMAC
        password.encode('utf-8'),  # Convert the password to bytes
        salt,  # Provide the salt
        100000,  # It is recommended to use at least 100,000 iterations of SHA-256
        dklen=128  # Get a 128 byte key
    )
    client.hash_hasla = key
    client.sol_hasla = salt
    client.save()

