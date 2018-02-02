from . import sqlalchemy_hive


class SparkSqlDialect(sqlalchemy_hive.HiveDialect):
    name = b'sparksql'
    supports_views = False

    def get_table_names(self, connection, schema=None, **kw):
        query = 'SHOW TABLES'
        if schema:
            query += ' IN ' + self.identifier_preparer.quote_identifier(schema)
        return [row[1] for row in connection.execute(query)]
