"""
MySQL database backend for Django.

Requires CyMySQL: https://github.com/nakagami/CyMySQL
"""
from __future__ import unicode_literals

try:
    from django.db.backends import BaseDatabaseFeatures
except ImportError: # 1.8
    from django.db.backends.base.features import BaseDatabaseFeatures
from django.utils.functional import cached_property
from django.utils import six

from mysql_cymysql.base import Database

try:
    import pytz
except ImportError:
    pytz = None


class DatabaseFeatures(BaseDatabaseFeatures):
    empty_fetchmany_value = []
    update_can_self_select = False
    allows_group_by_pk = True
    related_fields_match_type = True
    allow_sliced_subqueries = False
    has_bulk_insert = True
    has_select_for_update = True
    has_select_for_update_nowait = False
    supports_forward_references = False
    supports_long_model_names = False
    # XXX MySQL DB-API drivers currently fail on binary data on Python 3.
    supports_binary_field = six.PY2
    supports_microsecond_precision = False
    supports_regex_backreferencing = False
    supports_date_lookup_using_string = False
    can_introspect_binary_field = False
    can_introspect_boolean_field = False
    supports_timezones = False
    requires_explicit_null_ordering_when_grouping = True
    allows_auto_pk_0 = False
    allows_primary_key_0 = False
    uses_savepoints = True
    atomic_transactions = False
    supports_column_check_constraints = False

    def __init__(self, connection):
        super(DatabaseFeatures, self).__init__(connection)

    @cached_property
    def _mysql_storage_engine(self):
        "Internal method used in Django tests. Don't rely on this from your code"
        cursor = self.connection.cursor()
        cursor.execute('CREATE TABLE INTROSPECT_TEST (X INT)')
        # This command is MySQL specific; the second column
        # will tell you the default table type of the created
        # table. Since all Django's test tables will have the same
        # table type, that's enough to evaluate the feature.
        cursor.execute("SHOW TABLE STATUS WHERE Name='INTROSPECT_TEST'")
        result = cursor.fetchone()
        cursor.execute('DROP TABLE INTROSPECT_TEST')
        return result[1]

    @cached_property
    def can_introspect_foreign_keys(self):
        "Confirm support for introspected foreign keys"
        return self._mysql_storage_engine != 'MyISAM'

    @cached_property
    def has_zoneinfo_database(self):
        # MySQL accepts full time zones names (eg. Africa/Nairobi) but rejects
        # abbreviations (eg. EAT). When pytz isn't installed and the current
        # time zone is LocalTimezone (the only sensible value in this
        # context), the current time zone name will be an abbreviation. As a
        # consequence, MySQL cannot perform time zone conversions reliably.
        if pytz is None:
            return False

        # Test if the time zone definitions are installed.
        cursor = self.connection.cursor()
        cursor.execute("SELECT 1 FROM mysql.time_zone LIMIT 1")
        return cursor.fetchone() is not None

