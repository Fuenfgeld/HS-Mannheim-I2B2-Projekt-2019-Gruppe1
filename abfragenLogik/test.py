from pandas import DataFrame

import abfragenLogik.sqlGesamtanzahl as sqlGesamtanzahl
import abfragenLogik.sqlTemplates as sqlTemplates
import pandas as pd

# print(sg.gesamtanzahlPatienten())
# try:
#     print(st.anzahlPatProKriteriumBlatt("Hypertensive renal disease"))
# except:
#     print('Eltern')


sT = sqlTemplates.sqlTemplates()
sG = sqlGesamtanzahl.sqlGesamtanzahl()

print(sT.anzahlPatZweiKriterienAND("Essential hypertension", "Hypertensive renal disease"))

print(sT.anzahlPatZweiKriterienOR("Essential hypertension", "Hypertensive renal disease"))


