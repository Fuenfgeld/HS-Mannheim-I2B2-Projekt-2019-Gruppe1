import pandas as pd

from config import database
from backend.sql_logic import sql_strings
from backend.result_logic import result_merge


# used in app.py for the graphs
def generate_df_all_patients(queryBarLogicObject, case):
    if case is 'decimal':
        return pd.read_sql(queryBarLogicObject.get_all_patients_within_icd_list(), con=database.engine)
    elif case is 'sex_cd':
        df_temp = pd.read_sql(queryBarLogicObject.get_all_patients_within_icd_list(), con=database.engine)
        df_final = result_merge.merge_two_df(df_temp, case)
        return df_final
    elif case is 'language_cd':
        df_temp = pd.read_sql(queryBarLogicObject.get_all_patients_within_icd_list(), con=database.engine)
        df_final = result_merge.merge_two_df(df_temp, case)
        return df_final
    elif case is 'age_in_years_num':
        df_temp = pd.read_sql(queryBarLogicObject.get_all_patients_within_icd_list(),
                              con=database.engine)
        df_final = result_merge.merge_two_df(df_temp, case)
        return df_final
    elif case is 'race_cd':
        df_temp = pd.read_sql(queryBarLogicObject.get_all_patients_within_icd_list(), con=database.engine)
        df_final = result_merge.merge_two_df(df_temp, case)
        return df_final
    elif case is 'income_cd':
        df_temp = pd.read_sql(queryBarLogicObject.get_all_patients_within_icd_list(), con=database.engine)
        df_final = result_merge.merge_two_df(df_temp, case)
        return df_final
    elif case is 'concept_cd':
        df_temp = pd.read_sql(queryBarLogicObject.get_all_patients_within_icd_list(), con=database.engine)
        df_final = result_merge.merge_two_df(df_temp, case)
        return df_final

def generate_df_icd_code(queryBarLogicObject, value):
    return pd.read_sql(queryBarLogicObject.get_icd_code_from_name(value), con=database.engine)

# used in result_merge
def generate_df_sex_cd_patient_dimension():
    return pd.read_sql(sql_strings.SQL_i2b2_demodata_patient_dimension_sex_cd(), con=database.engine)

def generate_df_language_cd_patient_dimension():
    return pd.read_sql(sql_strings.SQL_i2b2_demodata_patient_dimension_language_cd(), con=database.engine)

def generate_df_age_in_years_num_patient_dimension():
    return pd.read_sql(sql_strings.SQL_i2b2_demodata_patient_dimension_age_in_years_num(), con=database.engine)

def generate_df_race_cd_patient_dimension():
    return pd.read_sql(sql_strings.SQL_i2b2_demodata_patient_dimension_race_cd(), con=database.engine)

def generate_df_income_cd_patient_dimension():
    return pd.read_sql(sql_strings.SQL_i2b2_demodata_patient_dimension_income_cd(), con=database.engine)

def generate_df_diag_all_observatio_fact_number():
    return pd.read_sql(sql_strings.SQL_i2b2_demodata_observation_fact_number(), con=database.engine)

def generate_df_diag_all_observatio_fact_icd():
    return pd.read_sql(sql_strings.SQL_i2b2_demodata_oservation_fact_icd(), con=database.engine)

def generate_df_only_pat_num():
    return pd.read_sql(sql_strings.SQL_i2b2_demodata_observation_pat_num(),con=database.engine)
