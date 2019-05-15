import abfragenLogik.sqlGesamtanzahl as sg
import abfragenLogik.sqlTemplates as st

#print(sg.gesamtanzahlPatienten())
try:
    print(st.anzahlPatProKriteriumBlatt("Hypertensive renal disease"))
except:
    print('Eltern')

print(st.anzahlPatZweiKriterienAND("Essential hypertension", "Hypertensive renal disease"))

print(st.anzahlPatZweiKriterienOR("Essential hypertension", "Hypertensive renal disease"))
