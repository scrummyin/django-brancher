from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from brancherer.base import DbNameMixin

class Command(DbNameMixin, BaseCommand):
    help = 'Lists all branches'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("SELECT datname FROM pg_database WHERE datname like '{}%';".format(self.get_db_name()))
            databases = cursor.fetchall()
            self.stdout.write("Your branched databases:")
            for datname in databases:
                self.stdout.write("\t{}".format(datname[0]))
