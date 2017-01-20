from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from brancherer.base import DbNameMixin


class Command(DbNameMixin, BaseCommand):
    help = 'Drops a database as long as it is not the default. Defaults to current git branch named database.'

    def handle(self, *args, **options):
        res = self.branch_name
        with connection.cursor() as cursor:
            cursor.execute("DROP DATABASE {name}_{branch}".format(branch=res, name=self.get_db_name))
