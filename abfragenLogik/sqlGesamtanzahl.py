import sqlalchemy as sa
import pandas as pd

engine = sa.create_engine('postgresql://i2b2:demouser@129.206.7.75:5432/i2b2')

def gesamtanzahlPatienten():
    abfrage = pd.read_sql("select distinct patient_num from i2b2.i2b2demodata.patient_dimension", con = engine)
    i = len(abfrage)
    return i

def gesamtanzahlMaenner():
    abfrage = pd.read_sql("select distinct patient_num from i2b2.i2b2demodata.patient_dimension where sex_cd = 'M'", con = engine)
    i = len(abfrage)
    return i

def gesamtanzahlFrauen():
    abfrage = pd.read_sql("select distinct patient_num from i2b2.i2b2demodata.patient_dimension where sex_cd = 'F'", con = engine)
    i = len(abfrage)
    return i








