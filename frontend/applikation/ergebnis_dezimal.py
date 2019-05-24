import dash
import dash_core_components as dcc
import dash_html_components as html
from backend.abfragenLogik import gesamt_anzahl

class ErgebnisDezimal():
    app = dash.Dash(__name__)

    gesamtAnzahl = gesamt_anzahl.GesamtAnzahl()

    layoutErgebnisDezimal = app.layout

    layoutErgebnisDezimal = html.Div([

        html.Div([html.H5(children="Anzahl Patienten: " + str(gesamtAnzahl.gesamtanzahlPatienten()))],
                 className='DivGesamtanzahl')
        ])