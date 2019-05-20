from backend.abfragenLogik import sql_templates
from backend.abfragenLogik import sql_verknuepfungen

sqlTemplates = sql_templates.SQLTemplates()
sqlVerknuepfung = sql_verknuepfungen.SQLVerknuepfung()

try:
    # rufe über Objekt auf
    # print("Alle Patienten")
    # print(gesamtAnzahl.gesamtanzahlPatienten())
    # print("Alle Männer")
    # print(gesamtAnzahl.gesamtanzahlMaenner())
    # print("Alle Frauen")
    # print(gesamtAnzahl.gesamtanzahlFrauen())

    # rufe über import auf
    print("Anzahl Patienten 'Essential hypertension': " +
          len(sqlTemplates.pat_df_ein_kriterium_blatt_i2b2('Essential hypertension')).__str__())
    print("Anzahl Patienten 'Essential hypertension AND Hypertensive renal disease': " +
          len(sqlVerknuepfung.anzahlPatZweiKriterienAND('Essential hypertension', 'Hypertensive renal disease')).__str__())
    print("Anzahl Patienten 'Essential hypertension OR Hypertensive renal disease': " +
          len(sqlVerknuepfung.anzahlPatZweiKriterienOR('Essential hypertension', 'Hypertensive renal disease')).__str__())

except:
    print('Eltern')

