import psycopg2 as pg
import pandas.io.sql as psql


connection = pg.connect(user="i2b2",
                        password="demouser",
                        host="129.206.7.75",
                        port="5432",
                        database="i2b2")

# cursor = connection.cursor()
#
# cursor.execute("SELECT version();")
#
# record = cursor.fetchone()
#
# print('You are connected to -', record)

df = psql.read_sql_query("SELECT * FROM i2b2demodata.visit_dimension", con=connection)
#    ^^^^^^^^^^^^^^^^^^^  workaround to not work with cursor
