import dash
import dash_core_components as dcc
import dash_html_components as html
#from SQL.selects import gesamt_anzahl
import pandas as pd
from backend.sql import string_sql
from backend.query_leiste import query_leiste


class ErgebnisDezimal:

    app = dash.Dash(__name__)


    layoutErgebnisDezimal = app.layout

    def setlayoutdezimal(self, df):
        layoutErgebnisDezimal = html.Div([

            html.Div([html.H5(children="Anzahl Patienten: " + str(len(df)))],
                     className='DivGesamtanzahl')])
        return layoutErgebnisDezimal