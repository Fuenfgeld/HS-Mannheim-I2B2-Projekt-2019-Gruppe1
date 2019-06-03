# class formattet_sql
def build_SQL_i2b2_demodata_observation_fact():
    return 'select distinct ob_fa.patient_num from i2b2metadata.i2b2 as i2b2 ' \
           'join i2b2demodata.observation_fact as ob_fa on i2b2.c_basecode = ob_fa.concept_cd ' \



def build_SQL_i2b2_demodata_observation_fact_2X():
    return 'SELECT distinct p1.patient_num FROM i2b2demodata.observation_fact as p1 ' \
           'join i2b2demodata.observation_fact as p2 ' \
           'on p1.patient_num = p2.patient_num ' \



def build_SQL_i2b2_demodata_patient_dimension():
    return 'select distinct patient_num from i2b2demodata.patient_dimension'


def build_SQL_i2b2_demodata_patient_dimension_sex_cd():
    return f'select sex_cd, patient_num from i2b2demodata.patient_dimension'


def build_SQL_i2b2_demodata_patient_dimension_language_cd():
    return f'select language_cd, patient_num from i2b2demodata.patient_dimension'


def build_SQL_i2b2_demodata_patient_dimension_age_in_years_num():
    return f'select age_in_years_num, patient_num from i2b2demodata.patient_dimension'


def build_SQL_i2b2_demodata_observation_fact_c_name():
    return 'select distinct i2b2.c_name from i2b2metadata.i2b2 as i2b2 ' \
           'join i2b2demodata.observation_fact  as of on i2b2.c_basecode=of.concept_cd '


def build_SQL_i2b2_metadata_icd10_icd9_c_basecode():
    return 'select distinct c_basecode from i2b2metadata.icd10_icd9 '