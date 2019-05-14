import dash
import dash_core_components as dcc
import dash_html_components as html

import sqlalchemy as sa
import pandas as pd

import formattedSQL as fs
import stringSQL as s

import database as db
engine = sa.create_engine("postgresql://i2b2:demouser@129.206.7.75:5432/i2b2")

sql1 = pd.read_sql("SELECT * FROM i2b2.i2b2metadata.icd10_icd9 WHERE c_hlevel = 1;", con=engine)
i = len(sql1)
print(i)

sql2 = pd.read_sql("select * from i2b2.i2b2demodata.patient_dimension where language_cd like 'eng%%'", con=engine)
a = len(sql2)
print(a)

Diag = "Diagnoses \ Diseases of the circulatory system"

sql3 = pd.read_sql(f"select distinct i2b2.i2b2demodata.patient_dimension.patient_num from i2b2.i2b2demodata.observation_fact "
                   f"join i2b2.i2b2metadata.icd10_icd9 on i2b2.i2b2metadata.icd10_icd9.c_basecode = i2b2.i2b2demodata.observation_fact.concept_cd "
                   f"join i2b2.i2b2demodata.patient_dimension on i2b2.i2b2demodata.observation_fact.patient_num = i2b2.i2b2demodata.patient_dimension.patient_num "
                   f"where i2b2.i2b2metadata.icd10_icd9.c_tooltip like '\{'Diag'+'%%'}\'", con=engine)
z = len(sql3)
print(z)


sql4 = pd.read_sql(fs.SQLBack(s.String11,s.String22,s.String33,s.String44,s.String55,s.String66,s.String77,s.String88), con=engine)
ä = len(sql4)
print(ä)

#curser = db.conn.cursor()
#curser.execute(fs.SQLJoin(s.String1, s.String2, s.String3, s.String4, s.String5, s.String6, s.String7))
#resulta = curser.rowcount
#curser.close()

#curser1 = db.conn.cursor()
#curser1.execute(
#    fs.SQLBack(s.String11, s.String22, s.String33, s.String44, s.String55, s.String66, s.String77, s.String88))
#resultb = curser1.rowcount
#curser1.close()

#print(resultb)
#print(resultb)

app = dash.Dash(external_stylesheets=['style.css'])
app.layout = html.Div([
#    html.Div([html.H1("Explorer")], className="Div1"),
#    html.Div([html.H1(resultb)], className="Div2"),
#    html.Div([
#        html.Div([html.H1(s.StringC)], className="StringC"),
#        html.Div(
#            [html.Div([html.H1(s.String5)], className="String5"), html.Div([html.H1(s.String7)], className="String7")],
#            className="String5_7")
#    ], className="Div3")
])

# Stop Flask Server Strg+C
if __name__ == '__main__':
    app.run_server(debug=True)
