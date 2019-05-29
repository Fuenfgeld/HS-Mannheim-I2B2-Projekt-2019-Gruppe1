import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from backend.result_logic import result_merge

colors = {
    'background': '#ffffff',
    'text': '#111111'
}

class graphLanguageDistribution:

    def set_layout_language_graph(self, df):
        dfNew = result_merge.merge_two_df(df, 'language_cd')
        count_english = dfNew.language_cd.str.count('english').sum()
        count_spanish = dfNew.language_cd.str.count('spanish').sum()
        count_german = dfNew.language_cd.str.count('german').sum()

        layoutLanguageDistribution = html.Div([

            dcc.Graph(
                id='language_distribution',
                figure=go.Figure(
                    data=[go.Bar(x=['Englisch', 'Spanisch', 'Deutsch'],
                                 y=[count_english, count_spanish, count_german],
                                 marker=dict(color=['#0066FF', '#CC3333','#FFCC00'],
                                             line=dict(color='#000000', width=2)),
                                 )
                          ],

                    layout=go.Layout(
                        title='Verteilung nach Muttersprache',

                    )
                )
            )
        ])

        return layoutLanguageDistribution

