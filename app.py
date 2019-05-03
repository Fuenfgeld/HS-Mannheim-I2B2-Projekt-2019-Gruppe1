import dash
import dash_core_components as dcc
import dash_html_components as html
import psycopg2 as psycopg2


dbname = "i2b2"
hostnr = "129.206.7.75"

conn = psycopg2.connect(
    host=hostnr,
    database=dbname,
    user="i2b2",
    password="demouser")

cur = conn.cursor()
cur.execute("SELECT count(sex_cd) FROM i2b2demodata.patient_dimension where sex_cd='F'")
resa = cur.fetchone()
resulta = resa[0]

cur1 = conn.cursor()
cur1.execute("SELECT count(sex_cd) from i2b2demodata.patient_dimension where sex_cd='M'")
resb = cur1.fetchone()
resultb = resb[0]

cur2 = conn.cursor()
cur2.execute("SELECT count(sex_cd) from i2b2demodata.patient_dimension")
resc = cur2.fetchone()
resultc = resc[0]


print(type(resulta))
print(type(resultb))
print(type(resultc))

a = 10;
print(type(a))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# rows = cur.fetchall()
#def dbausgabe():
 #   for r in rows:
  #      print(f"query_instance_id {r[0]}   query_master_id  {r[1]}")


app.layout = html.Div(children=[
    html.H1(children='DB Ausgabe'),

    html.H2("Frauen"),
    html.H2(resulta),


    dcc.Graph(
        id='männer-frauen-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [resulta, resultb, resulta], 'type': 'bar', 'name': 'Frauen'},
                {'x': [1, 2, 3], 'y': [resultc, resultc, resultb], 'type': 'bar', 'name': 'Männer'},
            ],
            'layout': {
                'title': 'Dash Männer vs Frauen Visualisieren'
            }
         }
    ),


dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )

])


if __name__ == '__main__':
    app.run_server(debug=True)

