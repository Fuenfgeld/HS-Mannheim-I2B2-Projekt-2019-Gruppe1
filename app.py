import dash
import dash_html_components as html
from SQL.selects.gesamt_anzahl import gesamtAnzahl
from SQL.selects.sql_verknüpfung import sqlVerknüpfung
from SQL.selects import sql_templates
from SQL.formatted import string_sql

gesamtAnzahl = gesamtAnzahl()
sqlVerknüpfung = sqlVerknüpfung()

# Ein Callback ist nichts anderes als ein Zeiger auf eine Funktion. Also eine Funktion, in der die Adresse einer anderen Funktion gespeichert wird.
# funclist = [gesamtAnzahl.gesamtanzahlPatienten(), gesamtAnzahl.gesamtanzahlMaenner(), gesamtAnzahl.gesamtanzahlFrauen()]

try:
    # rufe über Objekt auf
    # print("Alle Patienten")
    # print(gesamtAnzahl.gesamtanzahlPatienten())
    # print("Alle Männer")
    # print(gesamtAnzahl.gesamtanzahlMaenner())
    # print("Alle Frauen")
    # print(gesamtAnzahl.gesamtanzahlFrauen())

    # rufe über import auf

    # print(len(sql_templates.pat_df_ein_kriterium_blatt_cd('Essential hypertension')))
    # print(len(sql_templates.pat_df_ein_kriterium_blatt_i2b2('Essential hypertension')))

    # print(len(sql_templates.anzahlPatEinKriteriumEltern(string_sql.c_fullna)))
    # print(len(sql_templates.anzahlPatEinKriteriumEltern(string_sql.c_fullnam)))
    # print(len(sql_templates.anzahlPatEinKriteriumEltern(string_sql.c_fullname)))

    print(len(sqlVerknüpfung.anzahlPatZweiKriterienAND("Essential hypertension", "Hypertensive renal disease")))
    print(len(sqlVerknüpfung.anzahlPatZweiKriterienOR("Essential hypertension", "Hypertensive renal disease")))


    # 1 Patient
    # print(sqlVerknüpfung.anzahlPatZweiKriterienAND('Essential hypertension', 'Hypertensive renal disease'))
    # 40 Patienten
    # print(sqlVerknüpfung.anzahlPatZweiKriterienOR('Essential hypertension', 'Hypertensive renal disease'))

    # Versuch Eltern mit allen Unterknoten ausgeben
    # print(st.anzahlPatEinKriteriumEltern(c_fullname))
except:
    print('Eltern')


# app = dash.Dash(external_stylesheets=['style.css'])
# app.layout = html.Div([
#    html.Div([html.H1("Explorer")], className="Div1"),
#    html.Div([html.H1(resultb)], className="Div2"),
#    html.Div([
#        html.Div([html.H1(s.StringC)], className="StringC"),
#        html.Div(
#            [html.Div([html.H1(s.String5)], className="String5"), html.Div([html.H1(s.String7)], className="String7")],
#            className="String5_7")
#    ], className="Div3")
# ])

# Stop Flask Server Strg+C
# if __name__ == '__main__':
#     app.run_server(debug=True)
