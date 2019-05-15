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
            'Drag and Drop - Abfrageleiste ',
        ]),
        style={
            'width': '100%',
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
        , className='Div3'),

    html.Div([
        html.H3("Navigationsstruktur"),

    ], className="Div1"),

    html.Div([

        html.Div([
            html.Div([html.H5("Number of patients: " + str(sg.gesamtanzahlPatienten()))], className='Div4'),
            dcc.Graph(
                id="graph_close",
                figure={
                    'data': [
                        {'x': [1], 'y': [sg.gesamtanzahlFrauen()], 'type': 'bar', 'name': 'Female'},
                        {'x': [1], 'y': [sg.gesamtanzahlMaenner()], 'type': 'bar', 'name': 'Male'},
                    ],
                    'layout': {
                        'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font': {
                            'color': colors['text']
                        }
                    }
                }
            ),
            dcc.Graph(
                id="graph_close1",
                figure={
                    'data': [
                        {'x': [1], 'y': [1], 'type': 'markers', 'name': 'lol'},
                        {'x': [1], 'y': [2], 'type': 'bar', 'name': 'lol'},
                    ],
                    'layout': {
                        'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font': {
                            'color': colors['text']
                        }
                    }
                }
            ),
            dcc.Graph(id='device_usage',
                      figure=go.Figure(
                          data=[go.Pie(labels=['lol', 'lol'],
                                       values=[1, 1])],
                          layout=go.Layout(
                              title='Kreisdiagramm')
                      )),

        ], className="Div2"),

    ], className="row")
])

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == "__main__":
    app.run_server(debug=True, port=5001)
