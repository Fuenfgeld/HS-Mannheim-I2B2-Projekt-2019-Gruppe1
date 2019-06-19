# One criterium query
def SQL_i2b2_demodata_observation_fact_1_criterium():
    return 'select distinct ob_fa.patient_num from i2b2metadata.i2b2 as i2b2 ' \
           'join i2b2demodata.observation_fact as ob_fa on i2b2.c_basecode = ob_fa.concept_cd ' \
 \
        # get only the patient_num column from patient_dimension


def SQL_i2b2_demodata_patient_dimension_patient_num():
    return 'select distinct patient_num from i2b2demodata.patient_dimension'


# get special columns from patient_dimension for result_merge
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


# get name from ICD9-Code
def SQL_i2b2_demodata_observation_fact_c_name():
    return 'select distinct i2b2.c_name from i2b2metadata.i2b2 as i2b2 ' \
           'join i2b2demodata.observation_fact  as of on i2b2.c_basecode=of.concept_cd '


# get ICD9-Code from name
def SQL_i2b2_metadata_i2b2_c_basecode():
    return 'select distinct c_basecode from i2b2metadata.i2b2 '


# besides
# def SQL_i2b2_demodata_observation_fact_number():
#     return 'select count(concept_cd) as ccd from i2b2demodata.observation_fact ' \
#            'where concept_cd like \'ICD9:%%\' ' \
#            'group by concept_cd order by ccd desc limit 10'
#
#
# def SQL_i2b2_demodata_oservation_fact_icd():
#     return 'select concept_cd from i2b2demodata.observation_fact ' \
#            'where concept_cd like \'ICD9:%%\' ' \
#            'group by concept_cd order by count(concept_cd) desc limit 10';

# distinct oder group by machen das geliche
def SQL_i2b2_demodata_observation_pat_num():
    return 'select distinct concept_cd, patient_num from i2b2demodata.observation_fact ' \
           'where concept_cd like \'ICD9:%%\' ' \
           'group by concept_cd, patient_num'
