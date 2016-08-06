import cymysql
from django.db.backends.mysql import schema

class DatabaseSchemaEditor(schema.DatabaseSchemaEditor):

    def quote_value(self, value):
        return cymysql.converter.escape_item(value, 'utf-8')
