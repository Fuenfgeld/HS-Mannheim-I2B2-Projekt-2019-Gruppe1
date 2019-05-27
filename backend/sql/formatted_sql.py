from backend.sql import string_sql

# app
def build_SQL_patient_dimension():
    return string_sql.build_SQL_i2b2_patient_dimension()

def build_SQL_i2b2_observation_fact_krit1(Krit1):
    return string_sql.build_SQL_i2b2_observation_fact()+f'where i2b2.c_basecode = \'{Krit1}\''

def build_SQL_i2b2_observation_fact_krit2(Krit1, Krit2):
    return string_sql.build_SQL_i2b2_observation_fact_2X()+f'where p1.concept_cd = \'{Krit1}\' and p2.concept_cd = \'{Krit2}\''

