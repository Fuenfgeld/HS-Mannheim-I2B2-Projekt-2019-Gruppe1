import sqlalchemy as sa
import pandas as pd

engine = sa.create_engine('postgresql://i2b2:demouser@129.206.7.75:5432/i2b2')

def gesamtanzahlPatienten():
    abfrage = pd.read_sql("select distinct patient_num from i2b2.i2b2demodata.patient_dimension", con = engine)
    return len(abfrage)

def gesamtanzahlGeschlecht(sex_cd):
    abfrage = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.patient_dimension where sex_cd = \'{sex_cd}\'', con = engine)
    return len(abfrage)

def gesamtanzahlEthnie(race_cd):
    abfrage = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.patient_dimension where race_cd = \'{race_cd}\'', con = engine)
    return len(abfrage)

def gesamtanzahlFamilienstatus(marital_status_cd):
    abfrage = pd.read_sql(f'select distinct patient_num from i2b2.i2b2demodata.patient_dimension where marital_status_cd = \'{marital_status_cd}\'', con = engine)
    return len(abfrage)





