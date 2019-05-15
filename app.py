import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
#from iexfinance import get_historical_data
from dateutil.relativedelta import relativedelta
import plotly.graph_objs as go
import datetime
import pandas as pd
import requests
import database
import matplotlib as mlp
import matplotlib.pyplot as plt

import psycopg2 as psycopg2

import plotly.plotly as py
import plotly.graph_objs as go


# Server Connection (conn)
host = "129.206.7.75"
database = "i2b2"
user = "i2b2"
password = "demouser"
# import database as db

# Connection zum Server aufbauen
conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password)

# Suche die Anzahl der Datensätze von Frauen
curserAge = conn.cursor()
curserAge.execute("SELECT * FROM i2b2demodata.patient_dimension")
resultAge=curserAge.rowcount
curserAge.close()
print(resultAge)


curser1 = conn.cursor()
curser1.execute("SELECT sex_cd FROM i2b2demodata.patient_dimension where sex_cd='M'")
resultb=curser1.rowcount
curser1.close()
print(resultb)

curser = conn.cursor()
curser.execute("SELECT sex_cd FROM i2b2demodata.patient_dimension where sex_cd='F'")
resulta=curser.rowcount
resultNameF=curser.fetchone()
curser.close()
print(resulta)

curserName = conn.cursor()
curserName.execute("SELECT sex_cd FROM i2b2demodata.patient_dimension where sex_cd='M'")
resultName=curserName.fetchone()
curserName.close()
print(resultName)

resultSum = resultb+resulta

colors = {
    'background': '#ffffff',
    'text': '#111111'
}

import DB_Test as db  # import from the file with the database query
# import plotly.graph_objs as go
import row_generator as rg
import psycopg2 as psycopg2

start = datetime.datetime.today() - relativedelta(years=5)
end = datetime.datetime.today()

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')


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
                        for i in range(min(len(df),max_rows))
                    ]
                ),
                style={"height": "300px", "overflowY": "scroll"},
            ),
        ],
        style={"height": "100%"},)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H2("i2b2"),
        html.Img(src="/assets/LOGO.png")
    ], className="banner"),

    html.Div([html.H4("-------------------------------------------------------------------------ABFRAGELEISTE-------------------------------------------------------------------------")]),

    html.Div([
        html.H3("Patient dimension"),
        html.Ul(rg.add_list_items(db.dfPat))

    ], className="six columns"),

    html.Div([

        html.Div([
            html.H5("Ergebnis Dezimal: "+str(resultSum)),
            dcc.Graph(
                id="graph_close",
            figure={
             'data': [
                {'x': [1,2,3], 'y': [resulta], 'type': 'bar', 'name': "%s" % (resultNameF)},
                {'x': [1,2,3], 'y': [resultb], 'type': 'bar', 'name': "%s" % (resultName)},
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
                {'x': [1], 'y': [resultAge], 'type': 'markers', 'name': "%s" % (resultName)},
                {'x': [1], 'y': [resultb], 'type': 'bar', 'name': "%s" % (resultNameF)},
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
                        data=[go.Pie(labels=[resultName, resultNameF],
                                       values=[resultb, resulta])],
                        layout=go.Layout(
                              title='Kreisdiagramm')
                      )),

            dcc.Graph(
                    id='life-exp-vs-gdp',
                    figure={
#                      'data': [
#                             go.Scatter(
#                                 x=df[df['continent'] == i]['gdp per capita'],
#                                 y=df[df['continent'] == i]['life expectancy'],
#                                 text=df[df['continent'] == i]['country'],
#                                 mode='markers',
#                                 opacity=0.8,
#                                 marker={
#                                     'size': 15,
#                                     'line': {'width': 0.5, 'color': 'white'}
#                                 },
#                                 name=i
#                             ) for i in df.continent.unique()
#                         ],
                        'data': [
                            go.Scatter(
                                x=resultAge,
                                y=resultAge,
                                # text=curserAge[curserAge['age_in_years_num']['religion_cd']],
                                mode='markers',
                                opacity=0.8,
                                marker={
                                    'size': 15,
                                    'line': {'width': 0.5, 'color': 'white'}
                                },

                            )
                        ],
                        'layout': go.Layout(
                            xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                            yaxis={'title': 'Life Expectancy'},
                            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                            legend={'x': 0, 'y': 1},
                            hovermode='closest'
                        )
                    }
                )
        ], className="six columns"),



    ],className="row")
])
# app.layout = html.Div([
#     html.Div([
#
#         html.H2("Stock App"),
#         html.Img(src="/assets/stock-icon.png")
#     ], className="banner"),
#
#     html.Div([
#         dcc.Input(id="stock-input", value="SPY", type="text"),
#         html.Button(id="submit-button", n_clicks=0, children="Submit")
#     ]),
#
#     html.Div([
#         html.Div([
#             dcc.Graph(
#                 id="graph_close",
#             )
#         ], className="six columns"),
#
#         html.Div([
#             html.H3("Market News"),
#             generate_html_table()
#         ], className="six columns"),
#
#     ],className="row")
# ])

app.css.append_css({
    "external_url":"https://codepen.io/chriddyp/pen/bWLwgP.css"
})


# @app.callback(Output('graph_close', 'figure'),
#               [Input("", "n_clicks")],
#
#               )

# def update_fig(input_value):
#     df = get_historical_data(input_value, start=start, end=end, output_format="pandas")
#
#     trace_line = go.Scatter(x=list(df.index),
#                                 y=list(df.close),
#                                 #visible=False,
#                                 name="Close",
#                                 showlegend=False)
#
#     trace_candle = go.Candlestick(x=df.index,
#                            open=df.open,
#                            high=df.high,
#                            low=df.low,
#                            close=df.close,
#                            #increasing=dict(line=dict(color="#00ff00")),
#                            #decreasing=dict(line=dict(color="white")),
#                            visible=False,
#                            showlegend=False)
#
#     trace_bar = go.Ohlc(x=df.index,
#                            open=df.open,
#                            high=df.high,
#                            low=df.low,
#                            close=df.close,
#                            #increasing=dict(line=dict(color="#888888")),
#                            #decreasing=dict(line=dict(color="#888888")),
#                            visible=False,
#                            showlegend=False)
#
#     data = [trace_line, trace_candle, trace_bar]
#
#     updatemenus = list([
#         dict(
#             buttons=list([
#                 dict(
#                     args=[{'visible': [True, False, False]}],
#                     label='Line',
#                     method='update'
#                 ),
#                 dict(
#                     args=[{'visible': [False, True, False]}],
#                     label='Candle',
#                     method='update'
#                 ),
#                 dict(
#                     args=[{'visible': [False, False, True]}],
#                     label='Bar',
#                     method='update'
#                 ),
#             ]),
#             direction='down',
#             pad={'r': 10, 't': 10},
#             showactive=True,
#             x=0,
#             xanchor='left',
#             y=1.05,
#             yanchor='top'
#         ),
#     ])
#
#     layout = dict(
#         title=input_value,
#         updatemenus=updatemenus,
#         autosize=False,
#         xaxis=dict(
#             rangeselector=dict(
#                 buttons=list([
#                     dict(count=1,
#                          label='1m',
#                          step='month',
#                          stepmode='backward'),
#                     dict(count=6,
#                          label='6m',
#                          step='month',
#                          stepmode='backward'),
#                     dict(count=1,
#                          label='YTD',
#                          step='year',
#                          stepmode='todate'),
#                     dict(count=1,
#                          label='1y',
#                          step='year',
#                          stepmode='backward'),
#                     dict(step='all')
#                 ])
#             ),
#             rangeslider=dict(
#                 visible=True
#             ),
#             type='date'
#         )
#     )
#
    # return {
    #     "data": data,
    #     "layout": layout
    # }

if __name__=="__main__":
    app.run_server(debug=True, port=5001)