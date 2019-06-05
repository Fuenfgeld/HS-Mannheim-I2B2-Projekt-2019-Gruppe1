
import dash_core_components as dcc
import dash_html_components as html

class layoutNavigationBar:

    layout_navigation = html.Div([
        dcc.Input(id='input-box', placeholder='Eingabe', type='text', className="DivSuchen"),
        html.Button(id='add-button', children='Add', n_clicks=0),
        html.Div(id='clicked-button', children='del:0 add:0 last:nan', style={'display': 'none'}),
        html.Div(
            [html.Div(className='container'),
             html.Div(id='jstree-tree'),
             html.Div(id='jstree-result')]
        )

    ], className="DivNavigation")