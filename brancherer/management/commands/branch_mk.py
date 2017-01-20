from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from brancherer.base import DbNameMixin


class Command(DbNameMixin, BaseCommand):
    help = 'Creates another database branch by default uses your current git branch as the substring and your current default database as the template'

    def handle(self, *args, **options):
        res = self.branch_name
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE {name}_{branch} template {name}".format(branch=res, name=self.get_db_name()))
