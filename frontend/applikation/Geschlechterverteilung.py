import dash
import dash_core_components as dcc
import dash_html_components as html
from backend.abfragenLogik import gesamt_anzahl
from backend.baum import row_generator

colors = {
    'background': '#ffffff',
    'text': '#111111'
}

app = dash.Dash(__name__)

gesamtAnzahl = gesamt_anzahl.GesamtAnzahl()

app.layout = html.Div([

    html.Div([html.H5(children="Anzahl Patienten: " + str(gesamtAnzahl.gesamtanzahlPatienten()))],
             className='DivGesamtanzahl'),
    dcc.Graph(
        id="sex_distribution",
        figure={
            'data': [
                {'x': ['W'], 'y': [gesamtAnzahl.gesamtanzahlGeschlecht("F")], 'type': 'bar', 'name': 'Frauen'},
                {'x': ['M'], 'y': [gesamtAnzahl.gesamtanzahlGeschlecht("M")], 'type': 'bar', 'name': 'Männlich'},
            ],
            'layout': {
                'title': 'Geschlechterverteilung',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),

])