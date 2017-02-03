from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from brancher.base import DbNameMixin


class Command(DbNameMixin, BaseCommand):
    help = 'Lists all branches, a -> indicates current. (AKA what branch_it will run against)'

    def handle(self, *args, **options):
        self.print_databases(self.list_databases())

    def print_databases(self, databases=[]):
        self.stdout.write("Your branched databases:")
        for datname in databases:
            if datname == self.full_branched_db_name:
                self.stdout.write("->\t{}".format(datname))
            else:
                self.stdout.write("\t{}".format(datname))
