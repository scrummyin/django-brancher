from django.conf import settings


class DbNameMixin(object):
    def add_arguments(self, parser):
        pass

    def get_db_name(self):
        return settings.DATABASES['default']['NAME']

    @property
    def get_branch(self):
        return check_output('git rev-parse --abbrev-ref HEAD', shell=True)
