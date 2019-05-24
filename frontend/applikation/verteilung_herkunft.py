import dash
import dash_core_components as dcc
import dash_html_components as html
from backend.abfragenLogik import gesamt_anzahl
import plotly.graph_objs as go


class Herkunft():
    app = dash.Dash(__name__)

    gesamtAnzahl = gesamt_anzahl.GesamtAnzahl()

    layoutHerkunft = app.layout

    layoutHerkunft = html.Div([
        dcc.Graph(
            id='race_distribution',
            figure=go.Figure(
                data=[go.Pie(labels=['Afrikanisch', 'Europäisch', 'Asiatisch', 'Hispanisch', 'Indisch'],
                             values=[gesamtAnzahl.gesamtanzahlEthnie("black"),
                                     gesamtAnzahl.gesamtanzahlEthnie("white"),
                                     gesamtAnzahl.gesamtanzahlEthnie("asian"),
                                     gesamtAnzahl.gesamtanzahlEthnie("hispanic"),
                                     gesamtAnzahl.gesamtanzahlEthnie("indian")])],
                layout=go.Layout(
                    title='Ethnische Verteilung'
                )
            )
        )
    ])
