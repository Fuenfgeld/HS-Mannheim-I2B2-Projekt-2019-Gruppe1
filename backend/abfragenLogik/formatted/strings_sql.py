# file gesamt_anzahl.py
gesamtanzahlPatienten = "select distinct patient_num from i2b2.i2b2demodata.patient_dimension"

def build_SQL_gesamtanzahl_geschlecht(sex_cd):
    return f'select distinct patient_num from i2b2.i2b2demodata.patient_dimension where sex_cd = \'{sex_cd}\''

def build_SQL_gesamtanzahl_ehnie(race_cd):
    return f'select distinct patient_num from i2b2.i2b2demodata.patient_dimension where race_cd = \'{race_cd}\''

def build_SQL_gesamtanzahl_familienstatus(marital_status_cd):
    return f'select distinct patient_num from i2b2.i2b2demodata.patient_dimension where marital_status_cd = \'{marital_status_cd}\''


# file sql_templates.py
def build_SQL_concept_cd(name_char):
    return f'select concept_cd from i2b2.i2b2demodata.concept_dimension ' \
        f'where name_char = \'{name_char}\''

def build_SQL_c_basecode(name_char):
    return f'select distinct c_basecode from i2b2.i2b2metadata.i2b2 ' \
        f'where c_name = \'{name_char}\''

def build_SQL_icd(icd):
    return f'select distinct patient_num from i2b2.i2b2demodata.observation_fact ' \
        f'where concept_cd like \'{icd + "%%"}\''