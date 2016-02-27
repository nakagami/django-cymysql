from django.db.backends.mysql import schema

class DatabaseSchemaEditor(schema.DatabaseSchemaEditor):

    def quote_value(self, value):
        return self.connection.escape(value)
