from django.db.backends.mysql.features import DatabaseFeatures as BaseDatabaseFeatures
from django.utils.functional import cached_property

class DatabaseFeatures(BaseDatabaseFeatures):
    empty_fetchmany_value = []
    supports_paramstyle_pyformat = False
    can_clone_databases = False
    test_collations = {
        'ci': 'utf8_general_ci',
        'non_default': None,
        'swedish_ci': None,
    }

    @cached_property
    def django_test_skips(self):
        skips = super().django_test_skips()
        skips.update({
            "MySQL strict_mode does'nt work on CyMySQL": {
                'check_framework.test_database.test_database.DatabaseCheckTests'
            }
        })
        return skips
