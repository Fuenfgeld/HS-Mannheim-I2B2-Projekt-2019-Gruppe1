import pandas as pd
import config.database as database
import backend.abfragenLogik.formatted.strings_sql as string_sql

class GesamtAnzahl():

    def gesamtanzahlPatienten(self):
        abfrage = pd.read_sql(string_sql.gesamtanzahlPatienten, con = database.engine)
        return len(abfrage)

    def gesamtanzahlGeschlecht(self, sex_cd):
        abfrage = pd.read_sql(string_sql.build_SQL_gesamtanzahl_geschlecht(sex_cd), con = database.engine)
        return len(abfrage)

    def gesamtanzahlEthnie(self, race_cd):
        abfrage = pd.read_sql(string_sql.build_SQL_gesamtanzahl_ehnie(race_cd), con = database.engine)
        return len(abfrage)

    def gesamtanzahlFamilienstatus(self, marital_status_cd):
        abfrage = pd.read_sql(string_sql.build_SQL_gesamtanzahl_familienstatus(marital_status_cd), con = database.engine)
        return len(abfrage)





