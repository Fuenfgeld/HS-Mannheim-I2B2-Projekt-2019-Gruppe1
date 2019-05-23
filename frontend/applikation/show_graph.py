import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from backend.abfragenLogik import gesamt_anzahl

colors = {
    'background': '#ffffff',
    'text': '#111111'
}

class ShowGraph():
    gesamtAnzahl = gesamt_anzahl.GesamtAnzahl()
    app = dash.Dash(__name__)

    layoutGraph = app.layout

    layoutGraph = html.Div([

    html.Div([
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
        dcc.Graph(id='race_distribution',
                  figure=go.Figure(
                      data=[go.Pie(labels=['Afrikanisch', 'Europäisch', 'Asiatisch', 'Hispanisch', 'Indisch'],
                                   values=[gesamtAnzahl.gesamtanzahlEthnie("black"),
                                           gesamtAnzahl.gesamtanzahlEthnie("white"),
                                           gesamtAnzahl.gesamtanzahlEthnie("asian"),
                                           gesamtAnzahl.gesamtanzahlEthnie("hispanic"),
                                           gesamtAnzahl.gesamtanzahlEthnie("indian")])],
                      layout=go.Layout(
                          title='Ethnische Verteilung')
                  )
                  ),
        dcc.Graph(
            id='marital_status_distribution',
            figure={
                'data': [
                    {'x': ['Alleinstehend'], 'y': [gesamtAnzahl.gesamtanzahlFamilienstatus("single")], 'type': 'bar',
                     'name': 'Alleinstehend'},
                    {'x': ['Verheiratet'], 'y': [gesamtAnzahl.gesamtanzahlFamilienstatus("married")], 'type': 'bar',
                     'name': 'Verheiratet'},
                    {'x': ['Geschieden'], 'y': [gesamtAnzahl.gesamtanzahlFamilienstatus("divorced")], 'type': 'bar',
                     'name': 'Geschieden'},
                    {'x': ['Verwitwet'], 'y': [gesamtAnzahl.gesamtanzahlFamilienstatus("widow")], 'type': 'bar',
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

    ], className="DivErgebnis")

], className="row")

