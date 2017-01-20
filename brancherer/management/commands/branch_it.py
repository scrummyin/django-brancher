from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from subprocess import call
import os
from brancherer.base import DbNameMixin
import ipdb


class Command(DbNameMixin, BaseCommand):
    help = 'Run another django command using you current git branch as the branch name'

    def handle(self, *args, **options):
        with open(self.branched_settings_module_file, 'w') as f:
            f.write(self.formated_setting_file())
        os.environ["DJANGO_SETTINGS_MODULE"] = self.branched_settings_module
