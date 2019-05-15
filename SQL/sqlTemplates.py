import sqlalchemy as sa
import pandas as pd

engine = sa.create_engine("postgresql://i2b2:demouser@129.206.7.75:5432/i2b2")

#def anzahlPatEinKriteriumBlatt(name_char):
#    df = pd.read_sql(f'select concept_cd from i2b2.i2b2demodata.concept_dimension where name_char = \'{name_char}\'', con = engine)
#    s = "ICD9"
#    for n in range(0, 10):
#        # loc ist Auswahl an der Stelle 0,1,2... % .values ist direkt auf den Wert zugreifen
#        if s in df.loc[n].values[0]:
#            break
#    icd = df.loc[n].values[0]
#    df2 = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.observation_fact where concept_cd like \'{icd + "%%"}\'', con = engine)
#    return len(df2)

def anzahlPatEinKriteriumBlatt1(name_char):
    df = pd.read_sql(f'select c_basecode from i2b2.i2b2metadata.i2b2 where c_name = \'{name_char}\'', con = engine)
    s = "ICD9"
    for n in range(0, 10):
        if s in df.loc[n].values[0]:
            break


    icd = df.loc[n].values[0]
    df2 = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.observation_fact where concept_cd like \'{icd + "%%"}\'', con = engine)
    return df2

def anzahlPatEinKriteriumEltern(c_fullname):
    df = pd.read_sql(f'select distinct c_basecode from i2b2.i2b2metadata.i2b2 where c_fullname like \'{c_fullname + "%%"}\'', con=engine)
    s = "ICD9"
    col_names = ['A']
    df3 = pd.DataFrame(columns=col_names)
    for n in range(0, len(df)):
         if s in df.loc[n].values[0]:
            icd = df.loc[n].values[0]
            df2 = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.observation_fact where concept_cd like \'{icd + "%%"}\'',con=engine)
            for w in range(0, len(df2)):
                for e in range(0, len(df2)):
                    if df2.loc[w].values[0] not in df3.loc[e].values[0]:
                        df3.loc[e].values[0] = df2.loc[w].values[0]
    return df3

def anzahlPatZweiKriterienAND(name_char, name_char1):
    df1 = anzahlPatEinKriteriumBlatt1(name_char)
    df2 = anzahlPatEinKriteriumBlatt1(name_char1)
    AND = 0
    for n in range(0, len(df1)):
        m = df1.loc[n].values[0]
        for z in range(0, len(df2)):
            if m == df2.loc[z].values[0]:
                AND += 1
    return AND

def anzahlPatZweiKriterienOR(name_char, name_char1):
    df1 = anzahlPatEinKriteriumBlatt1(name_char)
    df2 = anzahlPatEinKriteriumBlatt1(name_char1)
    OR = 0
    AND = 0
    for n in range(0, len(df1)):
        m = df1.loc[n].values[0]
        for z in range(0, len(df2)):
            if m != df2.loc[z].values[0]:
                OR += 1
            elif m == df2.loc[z].values[0]:
                AND +=1


    return OR+AND