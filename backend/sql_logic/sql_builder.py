from backend.sql_logic import sql_strings


# used in query_bar_logic to get df with patient_nums from demodata.patient_dimension
def build_SQL_i2b2_patient_dimension_patient_num():
    return sql_strings.SQL_i2b2_demodata_patient_dimension_patient_num()


# used in query_bar_logic to get df with patient_num from demodata.observationfact
def build_SQL_i2b2_observation_fact_1_criterium(criterium):
    return sql_strings.SQL_i2b2_demodata_observation_fact_1_criterium() + f'where i2b2.c_basecode = \'{criterium}\''


def build_SQL_i2b2_observation_fact_2_criteria(criterium1, criterium2, connection):
    return f'select distinct patient_num from i2b2demodata.observation_fact obf1 where concept_cd = \'{criterium1}\' ' \
        f'{connection} exists (select \'{criterium1}\' from i2b2demodata.observation_fact obf2 ' \
        f'where obf1.patient_num = obf2.patient_num ' \
        f'and obf2.concept_cd = \'{criterium2}\')'


def build_SQL_i2b2_observation_fact_3_criteria(criterium1, criterium2, criterium3, connection1, connection2):
    if (connection1 == ' OR ') & (connection2 == ' OR '):
        return f'select distinct patient_num from i2b2demodata.observation_fact where concept_cd = \'{criterium1}\' ' \
            f'or concept_cd = \'{criterium2}\' or concept_cd = \'{criterium3}\''
    else:
        return f'select distinct patient_num from i2b2demodata.observation_fact obf1 where concept_cd = \'{criterium1}\' ' \
            f'{connection1} exists (select \'{criterium1}\' from i2b2demodata.observation_fact obf2 ' \
            f'where obf1.patient_num = obf2.patient_num ' \
            f'and obf2.concept_cd = \'{criterium2}\' {connection2} exists (select \'{criterium2}\' from ' \
            f'i2b2demodata.observation_fact obf3 where obf2.patient_num = obf3.patient_num ' \
            f'and obf3.concept_cd = \'{criterium3}\'))'


# get ICD9-Code from name
def build_SQL_i2b2_metadata_i2b2_code(name):
    return sql_strings.SQL_i2b2_metadata_i2b2_c_basecode() + f'where c_name = \'{name}\''


# get name from ICD9-Code
def build_SQL_i2b2_oservation_fact_1_criterium_name(criterium):
    return sql_strings.SQL_i2b2_demodata_observation_fact_c_name() + f'where i2b2.c_basecode = \'{criterium}\''


def build_SQL_i2b2_oservation_fact_2_criteria_name(criterium1, criterium2):
    return sql_strings.SQL_i2b2_demodata_observation_fact_c_name() + f'where i2b2.c_basecode = \'{criterium1}\' ' \
        f'and i2b2.c_basecode = \'{criterium2}\''
