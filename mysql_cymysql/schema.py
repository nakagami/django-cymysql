from django.db.backends.mysql import schema

class DatabaseSchemaEditor(schema.DatabaseSchemaEditor):

    def quote_value(self, value):
        import cymysql
        return cymysql.converters.escape_item(value, 'utf-8')
