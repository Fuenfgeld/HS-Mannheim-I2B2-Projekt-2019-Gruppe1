
import dash_core_components as dcc
import dash_html_components as html
from backend.tree import row_generator_level

class layoutNavigationBar:

    layoutNavigation = html.Div([
        dcc.Input(placeholder='Suche', type='text', className="DivSuchen"),
        html.Span([
           html.H5('ICD 10', className='caret'),
           html.Ul(row_generator_level.add_groundlevel(), className='nested'),
           html.Div(id='selected')])

    ], className="DivNavigation")