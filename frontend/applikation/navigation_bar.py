import dash
import dash_core_components as dcc
import dash_html_components as html
from backend.baum import row_generator

class ShowNavigation():
    app = dash.Dash(__name__,
                    external_stylesheets=['layout.css'],
                    external_scripts=['Zdropdown.js'])


    layoutNavigation = app.layout

    layoutNavigation = html.Div([
        html.Div(dcc.Input(placeholder='Suche', type='text', size= '61'), className="DivSuchleiste"),
        html.Span([
            html.H5('ICD 10', className='caret'),
            html.Ul(row_generator.add_groundlevel(), className='nested'),
            html.Div(id='selected')])

    ], className="DivNavigation")