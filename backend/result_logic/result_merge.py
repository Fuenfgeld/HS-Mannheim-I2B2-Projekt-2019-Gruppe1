import pandas as pd
from backend.sql import string_sql
from config import database

def build_df_patient_dimension():
    return pd.read_sql(string_sql.build_SQL_patient_dimension_sex_cd(), con=database.engine)

def merge_two_df(df1):
    return pd.merge(df1, build_df_patient_dimension(), how='inner', on='patient_num')