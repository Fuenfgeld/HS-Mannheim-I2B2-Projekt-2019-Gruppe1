# get only the patient_num column from patient_dimension:

def SQL_i2b2_demodata_patient_dimension_patient_num():
    return 'select distinct patient_num from i2b2demodata.patient_dimension'


# get special columns from patient_dimension for result_merge:

def SQL_i2b2_demodata_patient_dimension_sex_cd():
    return f'select sex_cd, patient_num from i2b2demodata.patient_dimension'


def SQL_i2b2_demodata_patient_dimension_race_cd():
    return f'select race_cd, patient_num from i2b2demodata.patient_dimension'


def SQL_i2b2_demodata_patient_dimension_income_cd():
    return f'select income_cd, patient_num from i2b2demodata.patient_dimension'


def SQL_i2b2_demodata_patient_dimension_language_cd():
    return f'select language_cd, patient_num from i2b2demodata.patient_dimension'


def SQL_i2b2_demodata_patient_dimension_age_in_years_num():
    return f'select age_in_years_num, patient_num from i2b2demodata.patient_dimension'


# distinct oder group by machen das gleiche:

def SQL_i2b2_demodata_observation_pat_num():
    return 'select distinct concept_cd, patient_num from i2b2demodata.observation_fact ' \
           'where concept_cd like \'ICD9:%%\' ' \
           'group by concept_cd, patient_num'


