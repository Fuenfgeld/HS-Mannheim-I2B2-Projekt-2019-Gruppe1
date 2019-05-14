import SQL.gesamtAnzahl as sg
import SQL.sqlTemplates as st

print(sg.gesamtanzahlPatienten())

try:
    print(st.anzahlPatEinKriteriumBlatt1("Cholelithiasis"))
    print(st.anzahlPatEinKriteriumBlatt("Cholelithiasis"))
except:
    print('Eltern')
