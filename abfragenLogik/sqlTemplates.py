import sqlalchemy as sa
import pandas as pd

engine = sa.create_engine("postgresql://i2b2:demouser@129.206.7.75:5432/i2b2")

def anzahlPatEinKriterium(name_char):
    df = pd.read_sql(f'select concept_cd from i2b2.i2b2demodata.concept_dimension where name_char = \'{name_char}\'', con = engine)
    icd = df.loc[0].values[0]
    df2 = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.observation_fact where concept_cd like \'{icd + "%%"}\'', con = engine)
    return len(df2)

def anzahlPatZweiKriterienAND():
    return 0

def anzahlPatZweiKriterienOR():
    return 0
