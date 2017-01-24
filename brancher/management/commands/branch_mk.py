from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from brancher.base import DbNameMixin


class Command(DbNameMixin, BaseCommand):
    help = 'Creates another database branch by default uses your current git branch as the substring and your current default database as the template'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE {branch} template {name}".format(branch=self.full_branched_db_name, name=self.get_db_name))
