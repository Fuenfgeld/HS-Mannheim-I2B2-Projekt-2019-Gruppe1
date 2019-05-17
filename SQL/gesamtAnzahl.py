from config import database as database
from SQL.formatted import stringSQL
import pandas as pd

class gesamtAnzahl:

    def gesamtanzahlPatienten(self):
        anzahlPatienten = pd.read_sql(stringSQL.gesamtanzahlPatienten, con=database.engine)
        return len(anzahlPatienten)

    def gesamtanzahlMaenner(self):
        anzahlMaenner = pd.read_sql(stringSQL.gesamtanzahlMaenner, con=database.engine)
        return len(anzahlMaenner)

    def gesamtanzahlFrauen(self):
        anzahlFrauen = pd.read_sql(stringSQL.gesamtanzahlFrauen, con=database.engine)
        return len(anzahlFrauen)
