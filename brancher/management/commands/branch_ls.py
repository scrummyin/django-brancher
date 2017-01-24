from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from brancher.base import DbNameMixin


class Command(DbNameMixin, BaseCommand):
    help = 'Lists all branches, a -> indicates current. (AKA what branch_it will run against)'

    def handle(self, *args, **options):
        self.change_defaults(**options)
        with connection.cursor() as cursor:
            cursor.execute("SELECT datname FROM pg_database WHERE datname like '{}%';".format(self.get_db_name))
            databases = cursor.fetchall()
            self.stdout.write("Your branched databases:")
            for datname in databases:
                result = datname[0]
                if result == self.full_branched_db_name:
                    self.stdout.write("->\t{}".format(datname[0]))
                else:
                    self.stdout.write("\t{}".format(datname[0]))
