import dash
import dash_core_components as dcc
import dash_html_components as html


class ShowAbfrageleiste():
    app = dash.Dash(__name__)
    layoutQuery = app.layout
    layoutQuery = html.Div([dcc.Upload(
        id='upload-data',
        children=html.Div([
            html.H5('Abfrageleiste '),
            html.H6("hjdf")
        ]),

        style={

            'width': '98,5%',
            'height': '70px',
            'lineHeight': '60px',
            'borderWidth': '2px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ), ]
        , className='DivAbfrageleiste')