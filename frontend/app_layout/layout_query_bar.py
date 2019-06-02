import dash_core_components as dcc
import dash_html_components as html


class layoutQueryBar:

    layout_query_bar = html.Div([dcc.Upload(
        children=html.Div([
            html.Div(id='output-container-button', children=''),
        ]), multiple=True), ]
        , id='querybar', className='DivAbfrageleiste')
