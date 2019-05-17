import pandas as pd
import config as config

class sqlTemplates():

    @staticmethod
    def patProKriteriumBlatt(name_char):
        df = pd.read_sql(f'select c_basecode from i2b2.i2b2metadata.i2b2 where c_name = \'{name_char}\'', con = config.engine)
        s = "ICD9"
        for n in range(0, 10):
            if s in df.loc[n].values[0]:
                break
        icd = df.loc[n].values[0]
        df2 = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.observation_fact where concept_cd like \'{icd + "%%"}\'', con = config.engine)
        return df2

    @staticmethod
    def anzahlPatProKriteriumBlatt(name_char):
        return len(sqlTemplates.patProKriteriumBlatt(name_char))

    @staticmethod
    def anzahlPatZweiKriterienAND(name_char1, name_char2):
        df1 = sqlTemplates.patProKriteriumBlatt(name_char1)
        df2 = sqlTemplates.patProKriteriumBlatt(name_char2)
        j = 0
        for n in range(0, len(df1)):
            for i in range(0, len(df2)):
                if df1.loc[n].values[0] == df2.loc[i].values[0]:
                    j += 1
        return j

    @staticmethod
    def anzahlPatZweiKriterienOR(name_char1, name_char2):
        df1 = sqlTemplates.patProKriteriumBlatt(name_char1)
        df2 = sqlTemplates.patProKriteriumBlatt(name_char2)
        j = len(df1) + len(df2)
        for n in range(0, len(df1)):
            for i in range(0, len(df2)):
                if df1.loc[n].values[0] == df2.loc[i].values[0]:
                    j -= 1
        return j

    @staticmethod
    def anzahlPatProKriteriumEltern():
        return 0
