""" Django command to wait for database to be available"""

from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    """ Django command wait for database """

    def handle(self, *args, **options):
        self.stdout.write("waiting for database ...")
        db_up = False
        while db_up is False:
            try:
                self.check(database=['default'])
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable, watting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))