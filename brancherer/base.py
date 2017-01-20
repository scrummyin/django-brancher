from django.conf import settings
from subprocess import check_output
import os


class DbNameMixin(object):
    def add_arguments(self, parser):
        pass

    @property
    def full_branched_db_name(self):
        return '{}_{}'.format(self.get_db_name, self.branch_name)

    @property
    def get_db_name(self):
        return settings.DATABASES['default']['NAME']

    @property
    def branch_name(self):
        return check_output('git rev-parse --abbrev-ref HEAD', shell=True).strip()

    @property
    def branched_settings_module(self):
        return 'branch_it_settings'

    @property
    def branched_settings_module_file(self):
        return os.path.join(os.getcwd(), '{}.py'.format(self.branched_settings_module))

    def settings_file_template(self):
        return "from {settings_file} import *; DATABASES['default']['NAME'] = '{base_db_name}_{db_branch}'"

    def formated_setting_file(self, **kwargs):
        settings_file_kwargs = self._default_settings_file_kwargs()
        settings_file_kwargs.update(**kwargs)
        return self.settings_file_template().format(**settings_file_kwargs)

    def _default_settings_file_kwargs(self):
        return {
                'settings_file': settings.SETTINGS_MODULE,
                'base_db_name': settings.DATABASES['default']['NAME'],
                'db_branch': self.branch_name,
        }
