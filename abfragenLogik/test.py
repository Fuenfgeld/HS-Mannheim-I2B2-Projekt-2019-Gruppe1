import abfragenLogik.sqlGesamtanzahl as sg
import abfragenLogik.sqlTemplates as st

#print(sg.gesamtanzahlPatienten())
try:
    print(st.anzahlPatEinKriteriumBlatt1("Cholelithiasis"))
except:
    print('Eltern')