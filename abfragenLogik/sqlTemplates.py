import sqlalchemy as sa
import pandas as pd

engine = sa.create_engine("postgresql://i2b2:demouser@129.206.7.75:5432/i2b2")

def patProKriteriumBlatt(name_char):
    df = pd.read_sql(f'select c_basecode from i2b2.i2b2metadata.i2b2 where c_name = \'{name_char}\'', con = engine)
    s = "ICD9"
    for n in range(0, 10):
        if s in df.loc[n].values[0]:
            break
    icd = df.loc[n].values[0]
    df2 = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.observation_fact where concept_cd like \'{icd + "%%"}\'', con = engine)
    return df2

def anzahlPatProKriteriumBlatt(name_char):
    return len(patProKriteriumBlatt(name_char))

def anzahlPatEinKriteriumEltern():
    return 0

def anzahlPatZweiKriterienAND(name_char1, name_char2):
    df1 = patProKriteriumBlatt(name_char1)
    df2 = patProKriteriumBlatt(name_char2)
    j = 0
    for n in range(0, len(df1)):
        m = df1.loc[n].values[0]
        for i in range(0, len(df2)):
            if m == df2.loc[i].values[0]:
                j += 1
    return j

def anzahlPatZweiKriterienOR(name_char1, name_char2):
    df1 = patProKriteriumBlatt(name_char1)
    df2 = patProKriteriumBlatt(name_char2)
    j = len(df1) + len(df2)
    for n in range(0, len(df1)):
        m = df1.loc[n].values[0]
        for i in range(0, len(df2)):
            if m == df2.loc[i].values[0]:
                j -= 1
    return j
