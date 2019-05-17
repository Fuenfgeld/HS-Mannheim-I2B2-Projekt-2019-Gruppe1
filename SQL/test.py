import SQL.sqlTemplates as st
from SQL.gesamtAnzahl import gesamtAnzahl
from SQL.sqlVerknüpfung import sqlVerknüpfung
from SQL import sqlTemplates

gesamtAnzahl = gesamtAnzahl()
sqlVerknüpfung = sqlVerknüpfung()

# Ein Callback ist nichts anderes als ein Zeiger auf eine Funktion. Also eine Funktion, in der die Adresse einer anderen Funktion gespeichert wird.
funclist = [gesamtAnzahl.gesamtanzahlPatienten(), gesamtAnzahl.gesamtanzahlMaenner(), gesamtAnzahl.gesamtanzahlFrauen()]

try:
    # über Objekt
    print(gesamtAnzahl.gesamtanzahlPatienten())
    print(gesamtAnzahl.gesamtanzahlMaenner())
    print(gesamtAnzahl.gesamtanzahlFrauen())

    # über import
    # 40 Patienten
    print(len(sqlTemplates.anzahlPatEinKriteriumBlatti2b2('Essential hypertension')))
    # 40 Patienten
    print(len(sqlTemplates.anzahlPatEinKriteriumBlattCD('Essential hypertension')))
    # 40 Patienten mi 4 Funktionen
    print(len(sqlTemplates.anzahlPatEinKriteriumBlatt(
        sqlTemplates.searchCodeEinKriteriumBlatt(
            sqlTemplates.concept_cdEinKriteriumBlatt(
                sqlTemplates.buildSQLEinKriteriumBlatt('Essential hypertension'))))))

    # Funktion die obrigen Zeilen vereint
    print(len(sqlTemplates.abstraktanzahlPatEinKriteriumBlattCD('Essential hypertension')))
    # 1 Patient
    print(sqlVerknüpfung.anzahlPatZweiKriterienAND('Essential hypertension', 'Hypertensive renal disease'))
    # 40 Patienten
    print(sqlVerknüpfung.anzahlPatZweiKriterienOR('Essential hypertension', 'Hypertensive renal disease'))

    # Versuch Eltern mit allen Unterknoten ausgeben
    # print(st.anzahlPatEinKriteriumEltern(c_fullname))
except:
    print('Eltern')
