import dash
import dash_core_components as dcc
import dash_html_components as html
from backend.sql import formatted_sql


class ShowAbfrageleiste():
    app = dash.Dash(__name__)
    layoutQuery = app.layout

    def showqueryleiste(self, result_name):
        layoutQuery = html.Div([dcc.Upload(
            id='upload-data',
            children=html.Div([
                html.H5(str(result_name.loc[0:]))
            ]),
            # style={
            #
            #     'width': '98,5%',
            #     'height': '70px',
            #     'lineHeight': '60px',
            #     'borderWidth': '2px',
            #     'borderStyle': 'dashed',
            #     'borderRadius': '5px',
            #     'textAlign': 'center',
            #     'margin': '10px'
            # },
            # Allow multiple files to be uploaded
            multiple=True
        ), ]
            , className='DivAbfrageleiste')

        return layoutQuery
