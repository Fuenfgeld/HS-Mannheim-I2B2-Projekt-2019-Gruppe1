# import level_dictionary_faster
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

d = dash
app = d.Dash(__name__, external_stylesheets=['style.css'],
             external_scripts=['tree_dropdown.js, bootstrap.js, jquery.js. jstree.js, selector.js'])

app.layout = html.Div(
    [html.Div(className='container'),
     html.Div(id='jstree-tree'),
     html.Div(id='jstree-result'),
     html.Div(dcc.Input(id='input-box', type='text', className='')),
     html.Button('Add to query', id='button'),
     html.Div(id='output-div')],
)


@app.callback(
    Output('output-div', 'children'),
    [Input('button', 'n_clicks')],
    [State('input-box', 'className')]
)
def update_output(n_clicks, value):
    return 'You selected {} and clicked it {} times'.format(
        value, n_clicks)


if __name__ == '__main__':
    app.run_server(debug=True)
