import dash
import dash_core_components as dcc
import dash_html_components as html
from dateutil.relativedelta import relativedelta
import datetime
import psycopg2 as psycopg2
import plotly.graph_objs as go
import DB_Test as db
import row_generator as rg


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




start = datetime.datetime.today() - relativedelta(years=5)
end = datetime.datetime.today()

# def generate_html_table(max_rows=10):
#
#     df = update_news()
#
#     return html.Div(
#         [
#             html.Div(
#                 html.Table(
#                     # Header
#                     [html.Tr([html.Th()])]
#                     +
#                     # Body
#                     [
#                         html.Tr(
#                             [
#                                 html.Td(
#                                     html.A(
#                                         df.iloc[i]["headline"],
#                                         href=df.iloc[i]["url"],
#                                         target="_blank"
#                                     )
#                                 )
#                             ]
#                         )
#                         for i in range(min(len(df),max_rows))
#                     ]
#                 ),
#                 style={"height": "300px", "overflowY": "scroll"},
#             ),
#         ],
#         style={"height": "100%"},)

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


        ], className="six columns"),



    ],className="row")
])


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