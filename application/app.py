import dash
import dash_core_components as dcc
import dash_html_components as html
from dateutil.relativedelta import relativedelta
import datetime
import pandas as pd
import requests
import plotly.graph_objs as go
import abfragenLogik.sqlGesamtanzahl as sg

colors = {
    'background': '#ffffff',
    'text': '#111111'
}

start = datetime.datetime.today() - relativedelta(years=5)
end = datetime.datetime.today()


def update_news():
    url = "https://api.iextrading.com/1.0/stock/market/news/last/5"
    r = requests.get(url)
    json_string = r.json()

    df = pd.DataFrame(json_string)
    df = pd.DataFrame(df[["headline", "url"]])

    return df


def generate_html_table(max_rows=10):
    df = update_news()

    return html.Div(
        [
            html.Div(
                html.Table(
                    # Header
                    [html.Tr([html.Th()])]
                    +
                    # Body
                    [
                        html.Tr(
                            [
                                html.Td(
                                    html.A(
                                        df.iloc[i]["headline"],
                                        href=df.iloc[i]["url"],
                                        target="_blank"
                                    )
                                )
                            ]
                        )
                        for i in range(min(len(df), max_rows))
                    ]
                ),
                style={"height": "300px", "overflowY": "scroll"},
            ),
        ],
        style={"height": "100%"}, )


app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H2("medical deGREEN"),
        html.Img(src="/assets/LOGO.png")
    ], className="banner"),

    html.Div([dcc.Upload(
        id='upload-data',
        children=html.Div([
            html.H5('Drag and Drop - Abfrageleiste '),
        ]),
        style={
            'width': '98,5%',
            'height': '150px',
            'lineHeight': '60px',
            'borderWidth': '2px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ), ]
        , className='DivAbfrageleiste'),

    html.Div([
        html.Div([html.H5("Suchen")], className="DivSuchleiste"),
        html.H5(children="Navigationsstruktur", style={
            'margin': '50px'
            }),

    ], className="DivNavigation"),

    html.Div([

        html.Div([
            html.Div([html.H5(children="Anzahl Patienten: " + str(sg.gesamtanzahlPatienten()))], className='DivGesamtanzahl'),
            dcc.Graph(
                id="sex_distribution",
                figure={
                    'data': [
                        {'x': ['W'], 'y': [sg.gesamtanzahlGeschlecht("F")], 'type': 'bar', 'name': 'Weiblich'},
                        {'x': ['M'], 'y': [sg.gesamtanzahlGeschlecht("M")], 'type': 'bar', 'name': 'Männlich'},
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
                                       values=[sg.gesamtanzahlEthnie("black"), sg.gesamtanzahlEthnie("white"),
                                               sg.gesamtanzahlEthnie("asian"), sg.gesamtanzahlEthnie("hispanic"),
                                               sg.gesamtanzahlEthnie("indian")])],
                          layout=go.Layout(
                              title='Ethnische Verteilung')
                      )
            ),
            dcc.Graph(
                id='marital_status_distribution',
                figure={
                    'data': [
                        {'x': ['Alleinstehend'], 'y': [sg.gesamtanzahlFamilienstatus("single")], 'type': 'bar', 'name': 'Alleinstehend'},
                        {'x': ['Verheiratet'], 'y': [sg.gesamtanzahlFamilienstatus("married")], 'type': 'bar', 'name': 'Verheiratet'},
                        {'x': ['Geschieden'], 'y': [sg.gesamtanzahlFamilienstatus("divorced")], 'type': 'bar', 'name': 'Geschieden'},
                        {'x': ['Verwitwet'], 'y': [sg.gesamtanzahlFamilienstatus("widow")], 'type': 'bar', 'name': 'Verwitwet'},
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
])

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == "__main__":
    app.run_server(debug=True, port=5001)
