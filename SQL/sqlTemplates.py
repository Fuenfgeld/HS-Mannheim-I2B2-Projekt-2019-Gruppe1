import pandas as pd
from config import database
from SQL.formatted import stringSQL

ICD9 = "ICD9"
ICD10 = "ICD10"


# über concept_dimension den ICD9 Code und über ICD9 die Patientennummern (DONE)
def anzahlPatEinKriteriumBlattCD(name_char):
    df1 = pd.read_sql(f'select concept_cd from i2b2.i2b2demodata.concept_dimension where name_char = \'{name_char}\'',
                      con=database.engine)
    for n in range(0, 10):
        if ICD9 in df1.loc[n].values[0]:
            break
    icd = df1.loc[n].values[0]
    df2 = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.observation_fact '
                      f'where concept_cd like \'{icd + "%%"}\'', con=database.engine)
    return df2


def pat_df_EinKriteriumBlattCD(name_char):
    buildsql = buildSQL_EinKriteriumBlatt(name_char)
    get_concept_cd = concept_cd_EinKriteriumBlatt(buildsql)
    icd_code = searchCode_EinKriteriumBlatt(get_concept_cd)
    patienten_df = patient_EinKriteriumBlatt(icd_code)
    return patienten_df


def buildSQL_EinKriteriumBlatt(name_char):
    buildsql = f'select concept_cd from i2b2.i2b2demodata.concept_dimension where name_char = \'{name_char}\''
    return buildsql


def concept_cd_EinKriteriumBlatt(buildsql):
    df = pd.read_sql(buildsql, con=database.engine)
    return df


def searchCode_EinKriteriumBlatt(df1):
    for n in range(0, len(df1)):
        if ICD9 in df1.loc[n].values[0]:
            break
    return df1.loc[n].values[0]


def patient_EinKriteriumBlatt(icd):
    df2 = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.observation_fact '
                      f'where concept_cd like \'{icd + "%%"}\'', con=database.engine)
    return df2


# über i2b2 den ICD9 Code und über ICD9 die Patientennummern (DONE)
def anzahlPatEinKriteriumBlatti2b2(name_char):
    df1 = pd.read_sql(f'select distinct c_basecode from i2b2.i2b2metadata.i2b2 '
                      f'where c_name = \'{name_char}\'', con=database.engine)
    for n in range(0, 10):
        if ICD9 in df1.loc[n].values[0]:
            break
    icd = df1.loc[n].values[0]
    df2 = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.observation_fact where concept_cd '
                      f'like \'{icd + "%%"}\'', con=database.engine)
    return df2


# pro basecode patienten rausholen und überprüfen ob doppelte
def anzahlPatEinKriteriumEltern(c_fullname):
    df = pd.read_sql(f'select distinct c_basecode from i2b2.i2b2metadata.i2b2 '
                     f'where c_fullname like \'{"%%" + c_fullname + "%%"}\'', con=database.engine)
    df = df.dropna()
    df3 = pd.DataFrame()
    for n in range(0, len(df)):
        if ICD10 not in df.loc[n].values[0]:
            icd = df.loc[n].values[0]
            df2 = pd.read_sql(f'select patient_num from i2b2.i2b2demodata.observation_fact '
                              f'where concept_cd like \'{icd + "%%"}\'', con=database.engine)
            df3 = df3.append(df2)
    df3 = df3.reset_index(drop=True)
    df3 = df3.drop_duplicates()
    print(df3)
    return len(df3)
