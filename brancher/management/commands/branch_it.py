from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from brancher.base import DbNameMixin
from django.core.management import call_command
from django import db
import argparse


class Command(DbNameMixin, BaseCommand):
    help = 'Run another django command using you current git branch as the branch name'
    _isolate = False
    _migrate = False

    def add_arguments(self, parser):
        parser.add_argument('-i', '--isolate', action='store_true', help="This will run create databse before the command and drop database afterwards")
        parser.add_argument('-m', '--migrate', action='store_true', help="Will run migrate before running the command you specified")
        parser.add_argument('subcommand', nargs=argparse.REMAINDER)
        super(Command, self).add_arguments(parser)

    def change_defaults(self, isolate=False, migrate=False, *args, **options):
        super(Command, self).change_defaults(*args, **options)
        self._isolate = isolate
        self._migrate = migrate

    def handle(self, *args, **options):
        self.change_defaults(**options)
        self.run_if_isolate(self.create_database)
        subcommand = options['subcommand']
        if not subcommand:
            raise CommandError('Please provide command')
        settings.DATABASES['default']['NAME'] = self.full_branched_db_name
        self.migrate_if_needed()
        try:
            call_command(*subcommand)
        except Exception as e:
            self.cleanup_if_needed()
            raise e
        self.cleanup_if_needed()

    def cleanup_if_needed(self):
        settings.DATABASES['default']['NAME'] = self.get_db_name
        db.connections.close_all()
        self.run_if_isolate(self.drop_database)

    def run_if_isolate(self, func):
        if self._isolate:
            func()

    def migrate_if_needed(self):
        if self._migrate:
            call_command('migrate')
