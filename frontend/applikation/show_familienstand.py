import dash
import dash_core_components as dcc
import dash_html_components as html

from backend.abfragenLogik import gesamt_anzahl

colors = {
    'background': '#ffffff',
    'text': '#111111'
}

class Familienstand():

    gesamtAnzahl = gesamt_anzahl.GesamtAnzahl()
    app = dash.Dash(__name__)

    layoutFamilienstand = app.layout

    layoutFamilienstand = html.Div([

        dcc.Graph(
            id='marital_status_distribution',
            figure={
                'data': [
                    {'x': ['Alleinstehend'], 'y': [gesamtAnzahl.gesamtanzahlFamilienstatus("single")],
                     'type': 'bar',
                     'name': 'Alleinstehend'},
                    {'x': ['Verheiratet'], 'y': [gesamtAnzahl.gesamtanzahlFamilienstatus("married")],
                     'type': 'bar',
                     'name': 'Verheiratet'},
                    {'x': ['Geschieden'], 'y': [gesamtAnzahl.gesamtanzahlFamilienstatus("divorced")],
                     'type': 'bar',
                     'name': 'Geschieden'},
                    {'x': ['Verwitwet'], 'y': [gesamtAnzahl.gesamtanzahlFamilienstatus("widow")],
                     'type': 'bar',
                     'name': 'Verwitwet'},
                ],
                'layout': {
                    'title': 'Verteilung nach Familienstatus',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    }
                }
            }
        )
    ])
