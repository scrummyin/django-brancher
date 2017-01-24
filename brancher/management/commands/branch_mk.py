from django.core.management.base import BaseCommand, CommandError
from brancher.base import DbNameMixin


class Command(DbNameMixin, BaseCommand):
    help = 'Creates another database branch by default uses your current git branch as the substring and your current default database as the template'

    def handle(self, *args, **options):
        self.change_defaults(**options)
        self.create_database()
