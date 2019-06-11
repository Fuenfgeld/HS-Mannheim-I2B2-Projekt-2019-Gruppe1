import dash_html_components as html
from backend.button import and_or


class layoutQueryBar:
    layout_button = html.Button(id='del-button', children=html.Img(src="/assets/papierkorb.png"), n_clicks=0, className='DivXbutton')
    layout_query_bar = html.Div([

            html.Div(id='query-bar', children=''),
            and_or.root_layout
        ], className='DivAbfrageleiste')





