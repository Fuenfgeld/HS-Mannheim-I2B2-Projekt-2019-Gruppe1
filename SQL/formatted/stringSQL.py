StringA = "i2b2.i2b2metadata.icd10_icd9"
StringB = "c_path"
StringC = "'\\Diagnoses\\'"

String1 = "i2b2.i2b2demodata.patient_dimension"
String2 = "i2b2.i2b2demodata.visit_dimension"
String3 = "patient_num"
String4 = "sex_cd"
String5 = "'F'"
String6 = "active_status_cd"
String7 = "'U'"

String11 = "patient_num"
String22 = "i2b2.i2b2demodata.observation_fact"
String33 = "i2b2.i2b2metadata.icd10_icd9"
String44 = "c_basecode"
String55 = "concept_cd"
String66 = "i2b2.i2b2demodata.patient_dimension"
String77 = "c_tooltip"
String88 = "Diagnoses \\ Diseases of the circulatory system"

#class gesamtAnzahl
gesamtanzahlPatienten = "select distinct patient_num from i2b2.i2b2demodata.patient_dimension"
gesamtanzahlMaenner = "select distinct patient_num from i2b2.i2b2demodata.patient_dimension where sex_cd = 'M'"
gesamtanzahlFrauen = "select distinct patient_num from i2b2.i2b2demodata.patient_dimension where sex_cd = 'F'"

#class sqlTemplates


#anzahlPatEinKriteriumBlattCD_df11 = f'select concept_cd from i2b2.i2b2demodata.concept_dimension where name_char = \'{name_char}\''
#anzahlPatEinKriteriumBlattCD_df2 = f'select distinct patient_num from i2b2.i2b2demodata.observation_fact where concept_cd like \'{icd + "%%"}\''

# Test für anzahlPatEinKriteriumEltern
c_fullna = '''_i2b2_Diagnoses_Symptoms_ signs_ and ill-defined conditions (780-799)_Nonspecific abnormal findings (790-796)_(793) Nonspecific abnormal findin'''
c_fullnam = '''_i2b2_Diagnoses_Symptoms_ signs_ and ill-defined conditions (780-799)_Nonspecific abnormal findings_(790-796)_'''
c_fullname = '''Nonspecific abnormal ele'''