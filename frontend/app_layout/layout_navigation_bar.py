
import dash_core_components as dcc
import dash_html_components as html
from deprecated import row_generator_level


class layoutNavigationBar:

    layout_navigation = html.Div([
        dcc.Input(id='input-box', placeholder='Suche', type='text', className="DivSuchen"),
        html.Button('Add', id='button'),
        # html.Span([
        #    html.H5('ICD 10', className='caret'),
        #    html.Ul(row_generator_level.add_groundlevel(), className='nested'),
        #    html.Div(id='selected')])

    ], className="DivNavigation")