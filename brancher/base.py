from django.conf import settings
from django.db import connection
from subprocess import check_output
import glob
import shutil
import os


class PostgresCompatMixin(object):
    @property
    def full_branched_db_name(self):
        return '{}_{}'.format(self.get_db_name, self.branch_name)

    def create_database(self):
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE {branch} template {name};".format(branch=self.full_branched_db_name, name=self.get_db_name))

    def drop_database(self):
        with connection.cursor() as cursor:
            cursor.execute("DROP DATABASE IF EXISTS {database};".format(database=self.full_branched_db_name))

    def list_databases(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT datname FROM pg_database WHERE datname like '{}%';".format(self.get_db_name))
            databases = cursor.fetchall()
            return [datname[0] for datname in databases]


class SqliteCompatMixin(object):
    @property
    def full_branched_db_name(self):
        head, ext = os.path.splitext(self.get_db_name)
        return '{}_{}{}'.format(self.get_db_name, self.branch_name, ext)

    def create_database(self):
        shutil.copyfile(self.get_db_name, self.full_branched_db_name)

    def drop_database(self):
        os.remove(self.full_branched_db_name)

    def list_databases(self):
        head, ext = os.path.splitext(self.get_db_name)
        return glob.glob('{}*'.format(head))


DBCompatMixin = PostgresCompatMixin
if connection.vendor == 'sqlite':
    DBCompatMixin = SqliteCompatMixin


class DbNameMixin(DBCompatMixin):
    _branch_name = None
    _db_name = None

    def add_arguments(self, parser):
        parser.add_argument('--branch_name', help="This overrides the git branch as the branch name")

    @property
    def get_db_name(self):
        if self._db_name is None:
            self._db_name = settings.DATABASES['default']['NAME']
        return self._db_name

    @property
    def branch_name(self):
        if self._branch_name is None:
            self._branch_name = check_output('git rev-parse --abbrev-ref HEAD', shell=True).strip()
        return self._branch_name

    def change_defaults(self, branch_name=None, **options):
        self._branch_name = branch_name
