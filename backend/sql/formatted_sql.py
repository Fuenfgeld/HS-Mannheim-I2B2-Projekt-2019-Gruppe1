from backend.sql import string_sql

# app
def build_SQL_i2b2_observation_fact():
    return string_sql.build_SQL_i2b2_patient_dimension()

def build_SQL_i2b2_observation_fact_krit1(Krit1):
    return string_sql.build_SQL_i2b2_observation_fact()+f'where i2b2.c_basecode = \'{Krit1}\''

def build_SQL_i2b2_observation_fact_krit2(Krit1, Krit2):
    return string_sql.build_SQL_i2b2_observation_fact()+f'where i2b2.c_basecode =\'{Krit1}\' and i2b2.c_basecode = \'{Krit2}\''

