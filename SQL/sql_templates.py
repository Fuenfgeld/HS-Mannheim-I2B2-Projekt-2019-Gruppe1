import pandas as pd
from config import database
from SQL.formatted import string_sql

ICD9 = "ICD9"
ICD10 = "ICD10"

# einen funktion hat eine funktion
def pat_df_ein_kriterium_blatt_cd(name_char):
    get_concept_cd = concept_cd_from_concept_dimension_ein_kriterium_blatt(name_char)
    icd_code = search_code_with_df(get_concept_cd)
    patienten_df = get_patient_with_icd(icd_code)
    return patienten_df


def pat_df_ein_kriterium_blatt_i2b2(name_char):
    get_c_basecode = c_basecode_from_i2b2_ein_kriterium_blatt(name_char)
    icd_code = search_code_with_df(get_c_basecode)
    patient_df = get_patient_with_icd(icd_code)
    return patient_df


def concept_cd_from_concept_dimension_ein_kriterium_blatt(name_char):
    df = pd.read_sql(string_sql.build_SQL_concept_cd(name_char), con=database.engine)
    return df


def c_basecode_from_i2b2_ein_kriterium_blatt(name_char):
    df = pd.read_sql(string_sql.build_SQL_c_basecode(name_char), con=database.engine)
    return df


def search_code_with_df(df):
    for n in range(0, len(df)):
        if ICD9 in df.loc[n].values[0]:
            break
    return df.loc[n].values[0]


def get_patient_with_icd(icd):
    df2 = pd.read_sql(string_sql.build_SQL_icd(icd), con=database.engine)
    return df2

# Erste Verision oder Verbessert

# über concept_dimension den ICD9 Code und über ICD9 die Patientennummern (DONE)
# def anzahlPatEinKriteriumBlattCD(name_char):
#     df1 = pd.read_sql(f'select concept_cd from i2b2.i2b2demodata.concept_dimension where name_char = \'{name_char}\'',
#                       con=database.engine)
#     for n in range(0, 10):
#         if ICD9 in df1.loc[n].values[0]:
#             break
#     icd = df1.loc[n].values[0]
#     df2 = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.observation_fact '
#                       f'where concept_cd like \'{icd + "%%"}\'', con=database.engine)
#     return df2


# über i2b2 den ICD9 Code und über ICD9 die Patientennummern (DONE)
# def pat_df_EinKriteriumBlatti2b2(name_char):
#     df1 = pd.read_sql(stringSQL.build_SQL_c_basecode(name_char), con=database.engine)
#     for n in range(0, 10):
#         if ICD9 in df1.loc[n].values[0]:
#             break
#     icd = df1.loc[n].values[0]
#     df2 = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.observation_fact where concept_cd '
#                       f'like \'{icd + "%%"}\'', con=database.engine)
#     return df2


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
