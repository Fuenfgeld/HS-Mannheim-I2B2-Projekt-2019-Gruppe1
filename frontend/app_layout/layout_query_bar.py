import dash_html_components as html


class layoutQueryBar:
    layout_button = html.Button(id='del-button', children='X', n_clicks=0, className='DivXbutton')
    layout_query_bar = html.Div([

            html.Div(id='query-bar', children='')
        ], className='DivAbfrageleiste')

