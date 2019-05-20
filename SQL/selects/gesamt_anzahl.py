from config import database as database
from SQL.formatted import string_sql
import pandas as pd

class gesamtAnzahl:

    def gesamtanzahlPatienten(self):
        anzahlPatienten = pd.read_sql(string_sql.gesamtanzahlPatienten, con=database.engine)
        return len(anzahlPatienten)

    def gesamtanzahlMaenner(self):
        anzahlMaenner = pd.read_sql(string_sql.gesamtanzahlMaenner, con=database.engine)
        return len(anzahlMaenner)

    def gesamtanzahlFrauen(self):
        anzahlFrauen = pd.read_sql(string_sql.gesamtanzahlFrauen, con=database.engine)
        return len(anzahlFrauen)
