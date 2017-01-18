from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from subprocess import check_output
from brancherer.base import DbNameMixin


class Command(DbNameMixin, BaseCommand):
    help = 'Creates another database branch by default uses your current git branch as the substring and your current default database as the template'

    def handle(self, *args, **options):
        res = check_output('git rev-parse --abbrev-ref HEAD', shell=True)
        self.stdout.write("{}".format(res))
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE {name}_{branch} template {name}".format(branch=res, name=self.get_db_name()))
