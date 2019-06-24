# import level_dictionary_faster
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

d = dash
app = d.Dash(__name__, external_stylesheets=['style.css'],
             external_scripts=['tree_dropdown.js, bootstrap.js, jquery.js. jstree.js, selector.js'])

nameList=[]

app.layout = html.Div(
    [html.Div(className='container'),
     html.Div(id='jstree-tree'),
     html.Div(id='jstree-result'),
     html.Div(dcc.Input(id='input-box', type='text')),
     html.Button('Add to query', id='button'),
     html.Div(id='output-div')],
)


@app.callback(
    Output('output-div', 'children'),
    [Input('button', 'n_clicks')],
    [State('input-box', 'value')]
)
def update_output(n_clicks, value):
    print(n_clicks, value)
    nameList.append('Lumbago')


if __name__ == '__main__':
    app.run_server(debug=True)
