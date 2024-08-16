from time import sleep
from typing import Any

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Wait for database conection'

    def handle(self, *args, **options):
        self.stdout.write('waiting for database...')
        db_conn = False

        while not db_conn:
            try:
                c = connection.cursor()
                c.execute('SELECT 1')
                db_conn = True
            except OperationalError:
                self.stdout.write('Database unavilable, waiting for a second...')
                sleep(1)
        self.stdout.write(self.style.SUCCESS('database available!'))