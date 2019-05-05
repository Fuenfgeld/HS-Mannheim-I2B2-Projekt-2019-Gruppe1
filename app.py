import dash
import dash_core_components as dcc
import dash_html_components as html
import psycopg2 as psycopg2

# Server Connection (conn)
host = "129.206.7.75"
database = "i2b2"
user = "i2b2"
password = "demouser"

# Connection zum Server aufbauen
conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password)

# Suche die Anzahl der Datensätze von Frauen
curser = conn.cursor()
curser.execute("SELECT sex_cd FROM i2b2demodata.patient_dimension where sex_cd='F'")
resulta = curser.rowcount
curser.close()

# Suche die Anzahl der Datensätze von Männer
cur = conn.cursor()
cur.execute("SELECT sex_cd from i2b2demodata.patient_dimension where sex_cd='M'")
resultb = cur.rowcount
cur.close()

# Suche die Anzahl der Datensätze von allen Patienten
cur = conn.cursor()
cur.execute("SELECT sex_cd from i2b2demodata.patient_dimension")
resultc = cur.rowcount
cur.close()

print("Resulta",resulta)
print("Resultb",resultb)
print("Resultc",resultc)

print("Typ von Resulta",type(resulta))
print("Typ von Resultb",type(resultb))
print("Typ von Resultc",type(resultc))

conn.close()


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[
    html.H1(children='DB Ausgabe'),

    html.H2("Frauen"),
    html.H2(resulta),


    dcc.Graph(
        id='frauen-männer-graph',
        figure={
            'data': [
                {'x': [1], 'y': [resulta], 'type': 'bar', 'name': 'Frauen'},
                {'x': [1], 'y': [resultb], 'type': 'bar', 'name': 'Männer'},
            ],
            'layout': {
                'title': 'Frauen und Männer Vergleich'
            }
         }
    )
])


if __name__ == '__main__':
   app.run_server(debug=True)

