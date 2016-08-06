import cymysql
from django.db.backends.mysql import schema

class DatabaseSchemaEditor(schema.DatabaseSchemaEditor):

    def quote_value(self, value):
        return cymysql.converters.escape_item(value, 'utf-8')
