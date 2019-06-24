import pandas as pd

from backend.sql_logic import sql_strings
from config import database


def generate_df_default():
    return pd.read_sql(sql_strings.SQL_i2b2_demodata_patient_dimension_patient_num(), con=database.engine)


def generate_df_two_criteria(con_list, df_list):
    if con_list[0] == 'AND':
        return pd.merge(df_list[0], df_list[1], how='inner', on='patient_num')
    if con_list[0] == 'OR':
        df_tmp = pd.concat([df_list[0], df_list[1]], ignore_index=True)
        df_tmp.drop_duplicates(subset='patient_num', keep='first', inplace=True)
        df_tmp.reset_index(drop=True)
        return df_tmp


def generate_df_three_criteria(con_list, df_list):
    if (con_list[0] == 'AND') & (con_list[1] == 'AND'):
        df_tmp = pd.merge(df_list[0], df_list[1], how='inner', on='patient_num')
        return pd.merge(df_tmp, df_list[2], how='inner', on='patient_num')
    if (con_list[0] == 'AND') & (con_list[1] == 'OR'):
        df_tmp = pd.merge(df_list[0], df_list[1], how='inner', on='patient_num')
        df_tmp1 = pd.concat([df_tmp, df_list[2]], ignore_index=True)
        df_tmp1.drop_duplicates(subset='patient_num', keep='first', inplace=True)
        df_tmp1.reset_index(drop=True)
        return df_tmp1
    if (con_list[0] == 'OR') & (con_list[1] == 'AND'):
        df_tmp = pd.merge(df_list[1], df_list[2], how='inner', on='patient_num')
        df_tmp1 = pd.concat([df_tmp, df_list[0]], ignore_index=True)
        df_tmp1.drop_duplicates(subset='patient_num', keep='first', inplace=True)
        df_tmp1.reset_index(drop=True)
        return df_tmp1
    if (con_list[0] == 'OR') & (con_list[1] == 'OR'):
        df_tmp = pd.concat([df_list[0], df_list[1]], ignore_index=True)
        df_tmp1 = pd.concat([df_tmp, df_list[2]], ignore_index=True)
        df_tmp1.drop_duplicates(subset='patient_num', keep='first', inplace=True)
        df_tmp1.reset_index(drop=True)
        return df_tmp1


# used in app.py for the graphs:

def generate_df_all_patients(queryBarLogicNewObject, resultMergeObject, case):
    if case is 'decimal':
        return queryBarLogicNewObject.get_actual_over_all_df()
    elif case is 'sex_cd':
        df_temp = queryBarLogicNewObject.get_actual_over_all_df()
        df_final = resultMergeObject.merge_two_df(df_temp, case)
        return df_final
    elif case is 'language_cd':
        df_temp = queryBarLogicNewObject.get_actual_over_all_df()
        df_final = resultMergeObject.merge_two_df(df_temp, case)
        return df_final
    elif case is 'age_in_years_num':
        df_temp = queryBarLogicNewObject.get_actual_over_all_df()
        df_final = resultMergeObject.merge_two_df(df_temp, case)
        return df_final
    elif case is 'race_cd':
        df_temp = queryBarLogicNewObject.get_actual_over_all_df()
        df_final = resultMergeObject.merge_two_df(df_temp, case)
        return df_final
    elif case is 'income_cd':
        df_temp = queryBarLogicNewObject.get_actual_over_all_df()
        df_final = resultMergeObject.merge_two_df(df_temp, case)
        return df_final
    elif case is 'concept_cd':
        df_temp = queryBarLogicNewObject.get_actual_over_all_df()
        df_final = resultMergeObject.merge_two_df(df_temp, case)
        return df_final


# used in result_merge:

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


def generate_df_only_pat_num():
    return pd.read_sql(sql_strings.SQL_i2b2_demodata_observation_pat_num(), con=database.engine)
