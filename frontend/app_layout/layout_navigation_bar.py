import dash_core_components as dcc
import dash_html_components as html
import visdcc


class layoutNavigationBar:
    layout_navigation = html.Div([
        dcc.Input(id='input-box', placeholder='Suche', type='text', className="DivSuchen", autoComplete='on'),
        html.Button('Add', id='button'),
        html.Button('Clear', id='clear'),
        html.Button('Do something', id='js-button'),
        visdcc.Run_js(id='javascript', run="alert('ITS HAPPENIIIING')"),
        html.Div([html.Div(className='container fade'),
        html.Div([html.Div(id='jstree-tree'),
                 html.Div(id='jstree-result', className='col-sm-6', hidden=True)],
                 className='row')],
                 className='modal-body',
                 )

        ], className="DivNavigation",)
