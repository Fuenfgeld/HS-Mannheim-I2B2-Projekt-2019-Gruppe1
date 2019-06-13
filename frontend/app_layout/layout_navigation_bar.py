
import dash_core_components as dcc
import dash_html_components as html


class layoutNavigationBar:
    layout_navigation = html.Div([
        dcc.Input(id='input-box', placeholder='Suche', type='text', className="DivSuchen", autoComplete='on'),
        html.Button('Add', id='button'),
        html.Button('Clear', id='clear'),
        html.Div([html.Div(className='container fade'),
        html.Div([html.Div(id='jstree-tree'),
                 html.Div(id='jstree-result', className='col-sm-6', hidden=True)],
                 className='row')],
                 className='modal-body',
                 )

        ], className="DivNavigation",)
