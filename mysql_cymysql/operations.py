from django.db.backends.mysql.operations import DatabaseOperations as BaseDatabaseOperations

class DatabaseOperations(BaseDatabaseOperations):

    def last_executed_query(self, cursor, sql, params):
        return getattr(cursor, '_last_executed', None)
