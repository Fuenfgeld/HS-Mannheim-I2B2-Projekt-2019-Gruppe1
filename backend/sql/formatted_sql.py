from backend.sql import string_sql

#get df-patient-num from i2b2/observationfact
def build_SQL_patient_dimension():
    return string_sql.build_SQL_i2b2_patient_dimension()

def build_SQL_i2b2_observation_fact_krit1(Krit1):
    return string_sql.build_SQL_i2b2_observation_fact()+f'where i2b2.c_basecode = \'{Krit1}\''

def build_SQL_i2b2_observation_fact_krit2(Krit1, Krit2):
    return string_sql.build_SQL_i2b2_observation_fact_2X()+f'where p1.concept_cd = \'{Krit1}\' and p2.concept_cd = \'{Krit2}\''

#get name from ICD9-Code
def build_name_i2b2_oservation_fact_krit1(Krit1):
    return string_sql.build_c_name_i2b2_oservation_fact()+f'where i2b2.c_basecode = \'{Krit1}\''

def build_name_i2b2_oservation_fact_krit2(Krit1, Krit2):
    return string_sql.build_c_name_i2b2_oservation_fact()+f'where i2b2.C_basecode = \'{Krit1}\' and i2b2.c_basecode = \'{Krit2}\''