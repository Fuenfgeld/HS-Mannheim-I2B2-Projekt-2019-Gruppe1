
import dash_core_components as dcc
import dash_html_components as html


class layoutNavigationBar:


    layout_navigation = html.Div([
        dcc.Input(id='input-box', placeholder='Suche', type='text', className="DivSuchen"),
        html.Button('Add', id='button'),
        html.Div(className='container'),
        html.Div(id='jstree-tree'),
        html.Div(id='jstree-result', hidden=True)

    ], className="DivNavigation")
