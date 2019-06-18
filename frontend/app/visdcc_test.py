import dash
import dash_html_components as html
import pandas as pd
import visdcc
from dash.dependencies import Input, Output


def generate_html_table_from_df(df, id):
    Thead = html.Thead(
        [html.Tr([html.Th(col) for col in df.columns])]
    )
    Tbody = html.Tbody(
        [html.Tr(
            [html.Td(df.iloc[i, j], id='{}_{}_{}'.format(id, i, j)) for j in range(len(df.columns))]
        ) for i in range(len(df))]
    )
    return html.Table([Thead, Tbody], id=id, className="display")


df = pd.DataFrame({'name': ['Jacky', 'Mei', 'Jay', 'Sandy', 'Jerry', 'Jimmy', 'Jeff',
                            'Jacky', 'Mei', 'Jay', 'Sandy', 'Jerry', 'Jimmy', 'Jeff',
                            'Jacky', 'Mei', 'Jay', 'Sandy', 'Jerry', 'Jimmy', 'Jeff'],
                   'age': [18, 71, 14, 56, 22, 28, 15,
                           18, 71, 14, 56, 22, 28, 15,
                           18, 71, 14, 56, 22, 28, 15]}, columns=['name', 'age'])

external_scripts = ['https://code.jquery.com/jquery-3.3.1.min.js',
                    'https://cdn.datatables.net/v/dt/dt-1.10.18/datatables.min.js']
external_stylesheets = ['https://cdn.datatables.net/v/dt/dt-1.10.18/datatables.min.css']

app = dash.Dash(external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Button('Add mousemove event', id='button'),
    visdcc.Run_js(id='javascript', run="$('#datatable').DataTable()"),
    html.Br(),
    html.Div(
        generate_html_table_from_df(df, id='datatable'),
        style={'width': '40%'}
    ),
    html.Div(id='output_div', className='Pineapple')
])


@app.callback(
    Output('javascript', 'run'),
    [Input('button', 'n_clicks')])
def myfun(x):
    if x is None: return ''
    return '''
    var target = document.getElementById('output_div')
    target.addEventListener('click', function(evt) {
        setProps({ 
            'event': {'x':$(event.target).innerHtml,
                      'y':evt.y }
        })
    })
    console.log(evt)
    '''


@app.callback(
    Output('output_div', 'children'),
    [Input('javascript', 'event')])
def myfun(x):
    print(x)
    return str(x)


if __name__ == '__main__':
    app.run_server(debug=True)
