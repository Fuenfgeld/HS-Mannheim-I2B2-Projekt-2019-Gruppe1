import psycopg2 as psycopg2


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