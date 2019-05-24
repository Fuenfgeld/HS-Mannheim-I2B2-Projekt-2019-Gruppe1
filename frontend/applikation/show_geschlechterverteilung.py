import dash
import dash_core_components as dcc
import dash_html_components as html
from backend.abfragenLogik import gesamt_anzahl

colors = {
    'background': '#ffffff',
    'text': '#111111'
}

class Geschlechterverteilung():
    app = dash.Dash(__name__)

    gesamtAnzahl = gesamt_anzahl.GesamtAnzahl()

    layoutGeschlechterverteilung = app.layout

    layoutGeschlechterverteilung = html.Div([

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
