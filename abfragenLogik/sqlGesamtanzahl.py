import pandas as pd
import config as config

class sqlGesamtanzahl():

    def gesamtanzahlPatienten(self):
        abfrage = pd.read_sql("select distinct patient_num from i2b2.i2b2demodata.patient_dimension", con = config.engine)
        return len(abfrage)

    def gesamtanzahlGeschlecht(self, sex_cd):
        abfrage = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.patient_dimension where sex_cd = \'{sex_cd}\'', con = config.engine)
        return len(abfrage)

    def gesamtanzahlEthnie(self, race_cd):
        abfrage = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.patient_dimension where race_cd = \'{race_cd}\'', con = config.engine)
        return len(abfrage)

    def gesamtanzahlFamilienstatus(self, marital_status_cd):
        abfrage = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.patient_dimension where marital_status_cd = \'{marital_status_cd}\'', con = config.engine)
        return len(abfrage)





