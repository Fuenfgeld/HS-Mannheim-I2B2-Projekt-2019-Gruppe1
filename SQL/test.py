import SQL.gesamtAnzahl as sg
import SQL.sqlTemplates as st


c_fullname = '''_i2b2_Diagnoses_Symptoms_ signs_ and ill-defined conditions (780-799)_Nonspecific abnormal findings (790-796)_(793) Nonspecific abnormal findin'''


try:
    print(st.anzahlPatZweiKriterienAND("Essential hypertension", "Hypertensive renal disease"))
    print(st.anzahlPatZweiKriterienOR("Essential hypertension", "Hypertensive renal disease"))

    print(c_fullname)
    print(st.anzahlPatEinKriteriumEltern(c_fullname))
except:
    print('Eltern')