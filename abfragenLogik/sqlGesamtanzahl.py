import pandas as pd
import config as config

class sqlGesamtanzahl():

    @staticmethod
    def gesamtanzahlPatienten():
        abfrage = pd.read_sql("select distinct patient_num from i2b2.i2b2demodata.patient_dimension", con = config.engine)
        return len(abfrage)

    @staticmethod
    def gesamtanzahlGeschlecht(sex_cd):
        abfrage = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.patient_dimension where sex_cd = \'{sex_cd}\'', con = config.engine)
        return len(abfrage)

    @staticmethod
    def gesamtanzahlEthnie(race_cd):
        abfrage = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.patient_dimension where race_cd = \'{race_cd}\'', con = config.engine)
        return len(abfrage)

    @staticmethod
    def gesamtanzahlFamilienstatus(marital_status_cd):
        abfrage = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.patient_dimension where marital_status_cd = \'{marital_status_cd}\'', con = config.engine)
        return len(abfrage)





