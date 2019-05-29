import dash_html_components as html

class layoutResultDecimal:

    def __init__(self):
        self.count_patients = str(134)

    def set_layout_decimal(self, df):
        if df is not None:
            self.count_patients = str(len(df))

        layoutResultDecimal = html.Div([

            html.Div([html.H5(children="Anzahl Patienten: " + self.count_patients)],
                     className='DivGesamtanzahl')])
        return layoutResultDecimal