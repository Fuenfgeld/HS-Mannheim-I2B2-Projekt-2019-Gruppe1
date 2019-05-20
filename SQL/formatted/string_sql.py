# class gesamt_anzahl.py
gesamtanzahlPatienten = "select distinct patient_num from i2b2.i2b2demodata.patient_dimension"
gesamtanzahlMaenner = "select distinct patient_num from i2b2.i2b2demodata.patient_dimension where sex_cd = 'M'"
gesamtanzahlFrauen = "select distinct patient_num from i2b2.i2b2demodata.patient_dimension where sex_cd = 'F'"


# Test für classe sqlTemplates Funk:anzahlPatEinKriteriumEltern



# class sqlTemplates
def build_SQL_concept_cd(name_char):
    return f'select concept_cd from i2b2.i2b2demodata.concept_dimension ' \
        f'where name_char = \'{name_char}\''

def build_SQL_c_basecode(name_char):
    return f'select distinct c_basecode from i2b2.i2b2metadata.i2b2 ' \
        f'where c_name = \'{name_char}\''

def build_SQL_icd(icd):
    return f'select distinct patient_num from i2b2.i2b2demodata.observation_fact ' \
        f'where concept_cd like \'{icd + "%%"}\''

