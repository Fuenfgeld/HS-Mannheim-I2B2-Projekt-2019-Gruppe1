import pandas as pd
from backend.sql import string_sql
from config import database

def build_df_sex_cd_patient_dimension():
    return pd.read_sql(string_sql.build_SQL_patient_dimension_sex_cd(), con=database.engine)

def build_df_language_cd_patient_dimension():
    return pd.read_sql(string_sql.build_SQL_patient_dimension_language_cd(), con=database.engine)

def build_df_age_in_years_num_patient_dimension():
    return pd.read_sql(string_sql.build_SQL_patient_dimension_age_in_years_num(), con=database.engine)

def merge_two_df(df, case):
    if case == 'sex_cd':
        return pd.merge(df, build_df_sex_cd_patient_dimension(), how='inner', on='patient_num')
    elif case == 'language_cd':
        return pd.merge(df, build_df_language_cd_patient_dimension(), how='inner', on='patient_num')
    elif case == 'age_in_years_num':
        return pd.merge(df, build_df_age_in_years_num_patient_dimension(), how='inner', on='patient_num')