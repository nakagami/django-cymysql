try:
    from django.db.backends.creation import BaseDatabaseCreation
except ImportError: # 1.8
    from django.db.backends.base.creation import BaseDatabaseCreation
from django.utils.functional import cached_property

class DatabaseCreation(BaseDatabaseCreation):

    @cached_property
    def data_types(self):
        # fallback propery for 1.6 and 1.7
        from mysql_cymysql.base import DatabaseWrapper
        return DatabaseWrapper._data_types

    def sql_table_creation_suffix(self):
        suffix = []
        if self.connection.settings_dict.get('TEST_CHARSET'):
             suffix.append('CHARACTER SET %s' % self.connection.settings_dict['TEST_CHARSET'])
        if self.connection.settings_dict.get('TEST_COLLATION'):
             suffix.append('COLLATE %s' % self.connection.settings_dict['TEST_COLLATION'])

        test_settings = self.connection.settings_dict.get('TEST')

        # checks for truth of test_settings are for django <=1.7a2 compatibility.
        if test_settings and test_settings['CHARSET']:
            suffix.append('CHARACTER SET %s' % test_settings['CHARSET'])
        if test_settings and test_settings['COLLATION']:
            suffix.append('COLLATE %s' % test_settings['COLLATION'])
        return ' '.join(suffix)

    def sql_for_inline_foreign_key_references(self, model, field, known_models, style):
        "All inline references are pending under MySQL"
        return [], True

    def sql_destroy_indexes_for_fields(self, model, fields, style):
        if len(fields) == 1 and fields[0].db_tablespace:
            tablespace_sql = self.connection.ops.tablespace_sql(fields[0].db_tablespace)
        elif model._meta.db_tablespace:
            tablespace_sql = self.connection.ops.tablespace_sql(model._meta.db_tablespace)
        else:
            tablespace_sql = ""
        if tablespace_sql:
            tablespace_sql = " " + tablespace_sql

        field_names = []
        qn = self.connection.ops.quote_name
        for f in fields:
            field_names.append(style.SQL_FIELD(qn(f.column)))

        index_name = "%s_%s" % (model._meta.db_table, self._digest([f.name for f in fields]))

        from django.db.backends.util import truncate_name

        return [
            style.SQL_KEYWORD("DROP INDEX") + " " +
            style.SQL_TABLE(qn(truncate_name(index_name, self.connection.ops.max_name_length()))) + " " +
            style.SQL_KEYWORD("ON") + " " +
            style.SQL_TABLE(qn(model._meta.db_table)) + ";",
        ]
