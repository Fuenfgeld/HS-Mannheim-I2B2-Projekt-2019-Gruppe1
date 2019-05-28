# class formattet_sql
def build_SQL_i2b2_observation_fact():
    return 'select distinct ob_fa.patient_num from i2b2metadata.i2b2 as i2b2 ' \
           'join i2b2demodata.observation_fact as ob_fa on i2b2.c_basecode = ob_fa.concept_cd ' \

def build_SQL_i2b2_observation_fact_2X():
    return 'SELECT distinct p1.patient_num FROM i2b2demodata.observation_fact as p1 ' \
           'join i2b2demodata.observation_fact as p2 ' \
           'on p1.patient_num = p2.patient_num ' \


def build_SQL_i2b2_patient_dimension():
    return 'select distinct patient_num from i2b2demodata.patient_dimension'

#letzte merge auf patiente_dimension
def build_SQL_patient_dimension_sex_cd():
    return f'select sex_cd, patient_num from i2b2demodata.patient_dimension'

def build_c_name_i2b2_oservation_fact():
    return 'select distinct i2b2.c_name from i2b2metadata.i2b2 as i2b2 ' \
           'join i2b2demodata.observation_fact  as of on i2b2.c_basecode=of.concept_cd '