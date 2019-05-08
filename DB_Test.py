import pandas.io.sql as psql
import psycopg2 as pg

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

dfPat = psql.read_sql_query("SELECT * FROM i2b2demodata.patient_dimension", con=connection)
dfVis = psql.read_sql_query("SELECT * FROM i2b2demodata.visit_dimension", con=connection)
#    ^^^^^^^^^^^^^^^^^^^  workaround to not work with cursor
