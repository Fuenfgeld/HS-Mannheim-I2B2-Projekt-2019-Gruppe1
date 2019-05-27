import pandas as pd
from backend.sql import string_sql
from config import database

def builddfpd():
    return pd.read_sql(string_sql.build_SQL_patient_dimension_sex_cd(), con=database.engine)

def mergezweidf(df1):
    return pd.merge(df1, builddfpd(), how='inner', on='patient_num')