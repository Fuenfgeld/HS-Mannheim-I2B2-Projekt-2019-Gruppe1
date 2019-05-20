from backend.abfragenLogik import gesamt_anzahl as gesamt_anzahl
from backend.abfragenLogik import sql_templates as sql_templates
from backend.abfragenLogik import sql_verknuepfungen as sql_verknuepfungen

gesamtAnzahl = gesamt_anzahl.GesamtAnzahl()
sqlVerknuepfung = sql_verknuepfungen.SQLVerknuepfung()

# print(sg.gesamtanzahlPatienten())
# try:
#     print(st.anzahlPatProKriteriumBlatt("Hypertensive renal disease"))
# except:
#     print('Eltern')


sT = sqlTemplates.sqlTemplates()
sG = sqlGesamtanzahl.sqlGesamtanzahl()

print(sT.anzahlPatZweiKriterienAND("Essential hypertension", "Hypertensive renal disease"))

print(sT.anzahlPatZweiKriterienOR("Essential hypertension", "Hypertensive renal disease"))

# Ein Callback ist nichts anderes als ein Zeiger auf eine Funktion. Also eine Funktion, in der die Adresse einer anderen Funktion gespeichert wird.
funclist = [gesamtAnzahl.gesamtanzahlPatienten(), gesamtAnzahl.gesamtanzahlMaenner(), gesamtAnzahl.gesamtanzahlFrauen()]

try:
    # rufe über Objekt auf
    # print("Alle Patienten")
    # print(gesamtAnzahl.gesamtanzahlPatienten())
    # print("Alle Männer")
    # print(gesamtAnzahl.gesamtanzahlMaenner())
    # print("Alle Frauen")
    # print(gesamtAnzahl.gesamtanzahlFrauen())

    # rufe über import auf
    print(len(sql_templates.pat_df_ein_kriterium_blatt_cd('Essential hypertension')))
    print(len(sql_templates.pat_df_ein_kriterium_blatt_i2b2('Essential hypertension')))

    # 1 Patient
    # print(sqlVerknüpfung.anzahlPatZweiKriterienAND('Essential hypertension', 'Hypertensive renal disease'))
    # 40 Patienten
    # print(sqlVerknüpfung.anzahlPatZweiKriterienOR('Essential hypertension', 'Hypertensive renal disease'))

    # Versuch Eltern mit allen Unterknoten ausgeben
    # print(st.anzahlPatEinKriteriumEltern(c_fullname))
except:
    print('Eltern')

