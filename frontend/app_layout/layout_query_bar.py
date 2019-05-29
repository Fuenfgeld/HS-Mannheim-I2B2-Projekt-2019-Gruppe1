
import dash_core_components as dcc
import dash_html_components as html

class layoutQueryBar:

    def fill_query_bar(self, name_list):
        if len(name_list)==1:
            layoutQuery = html.Div([dcc.Upload(
                children=html.Div([
                    html.P(name_list[0]),
                ]), multiple=True), ]
                , className='DivAbfrageleiste')
            return layoutQuery
        elif len(name_list)==3:
            layoutQuery = html.Div([dcc.Upload(
                children=html.Div([
                    html.P(name_list[0]),
                    html.P(name_list[1]),
                    html.P(name_list[2])
                ]), multiple=True), ]
                , className='DivAbfrageleiste')
            return layoutQuery