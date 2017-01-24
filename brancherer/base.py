from django.conf import settings
from subprocess import check_output
import os


class DbNameMixin(object):
    _branch_name = None

    def add_arguments(self, parser):
        parser.add_argument('--branch_name')

    @property
    def full_branched_db_name(self):
        return '{}_{}'.format(self.get_db_name, self.branch_name)

    @property
    def get_db_name(self):
        return settings.DATABASES['default']['NAME']

    @property
    def branch_name(self):
        if self._branch_name is None:
            self._branch_name = check_output('git rev-parse --abbrev-ref HEAD', shell=True).strip()
        return self._branch_name

    def handle(self, *args, **options):
        self._branch_name = options['branch_name']
