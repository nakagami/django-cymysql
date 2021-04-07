from django.db.backends.mysql.features import DatabaseFeatures as BaseDatabaseFeatures


class DatabaseFeatures(BaseDatabaseFeatures):
    empty_fetchmany_value = []
    supports_paramstyle_pyformat = False
    can_clone_databases = False
    test_collations = {
        'ci': 'utf8_general_ci',
        'non_default': None,
        'swedish_ci': None,
    }
