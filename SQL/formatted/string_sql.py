# class gesamt_anzahl.py
gesamtanzahlPatienten = "select distinct patient_num from i2b2.i2b2demodata.patient_dimension"
gesamtanzahlMaenner = "select distinct patient_num from i2b2.i2b2demodata.patient_dimension where sex_cd = 'M'"
gesamtanzahlFrauen = "select distinct patient_num from i2b2.i2b2demodata.patient_dimension where sex_cd = 'F'"


# Test für classe sqlTemplates Funk:anzahlPatEinKriteriumEltern
# c_fullna = '''_i2b2_Diagnoses_Symptoms_ signs_ and ill-defined conditions (780-799)_Nonspecific abnormal findings (790-796)_(793) Nonspecific abnormal findin'''
# c_fullnam = '''_i2b2_Diagnoses_Symptoms_ signs_ and ill-defined conditions (780-799)_Nonspecific abnormal findings_(790-796)_'''
# c_fullname = '''Nonspecific abnormal ele'''


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

