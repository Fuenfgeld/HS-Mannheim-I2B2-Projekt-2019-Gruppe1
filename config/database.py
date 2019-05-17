import psycopg2 as psycopg2
import sqlalchemy as sa


host = "129.206.7.75"
database = "i2b2"
user = "i2b2"
password = "demouser"


# Connection zum Server aufbauen
conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password)

engine = sa.create_engine('postgresql://i2b2:demouser@129.206.7.75:5432/i2b2')