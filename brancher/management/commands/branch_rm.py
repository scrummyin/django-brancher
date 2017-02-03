from django.core.management.base import BaseCommand, CommandError
from brancher.base import DbNameMixin


class Command(DbNameMixin, BaseCommand):
    help = 'Drops a database as long as it is not the default. Defaults to current git branch named database.'

    def handle(self, *args, **options):
        self.change_defaults(**options)
        self.drop_database()
