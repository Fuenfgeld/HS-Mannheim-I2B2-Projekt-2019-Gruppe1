import dash_html_components as html

class layoutResultDecimal:

    def set_layout_decimal(self, df):
        count_patients = str(len(df))

        layoutResultDecimal = html.Div([

            html.Div([html.H5(children="Anzahl Patienten: " + count_patients)],
                     className='DivGesamtanzahl')])
        return layoutResultDecimal