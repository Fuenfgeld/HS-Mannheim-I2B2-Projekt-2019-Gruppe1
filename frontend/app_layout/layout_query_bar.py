import dash_html_components as html


class layoutQueryBar:
    layout_delete_button = html.Button(id='del-button', children=html.Img(src="/assets/papierkorb.png"), n_clicks=0,
                                       className='DivXbutton')
    layout_criteria_one = html.Div(id='criteria1-div', children='', className='DivKriterium1', hidden=True)
    layout_connection1_button = html.Button(id='and-button', children=html.H5('AND'), n_clicks=0,
                                            className='DivVerbindung1Button', style={'display': 'none'})
    layout_criteria_two = html.Div(id='criteria2-div', children='', className='DivKriterium2', hidden=True)
    layout_query_bar = html.Div(id='query-bar', className='DivAbfrageleiste')
