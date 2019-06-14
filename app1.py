# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output

import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Button(id='btn-1', children='Button 1', n_clicks=0),
    html.Div(id='con', children='')
])

ic = ['A', 'AND', 'B']

@app.callback(
    Output('con', 'children'),
    [Input('btn-1', 'n_clicks')]
)
def displayClick(n_clicks):
    msg = ic[0] + ic[1] + ic[2]
    if int(n_clicks) % 2 == 0:
        ic[1] = 'AND'
        msg = ic[0]+ic[1]+ic[2]
    else:
        ic[1] = 'OR'
        msg = ic[0] + ic[1] + ic[2]
    return html.Div([
        html.Div('{}'.format(msg))
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
