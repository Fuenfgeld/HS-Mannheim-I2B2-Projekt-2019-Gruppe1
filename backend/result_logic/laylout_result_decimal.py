import dash_html_components as html

class ErgebnisDezimal:

    def set_layout_decimal(self, df):
        layoutErgebnisDezimal = html.Div([

            html.Div([html.H5(children="Anzahl Patienten: " + str(len(df)))],
                     className='DivGesamtanzahl')])
        return layoutErgebnisDezimal