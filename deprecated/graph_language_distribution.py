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
        df_new = result_merge.merge_two_df(df, 'language_cd')
        count_english_new = df_new.language_cd.str.count('english').sum()
        count_spanish_new = df_new.language_cd.str.count('spanish').sum()
        count_german_new = df_new.language_cd.str.count('german').sum()

        df_over_all = result_merge.generate_df_language_cd_patient_dimension()
        count_english_over_all = df_over_all.language_cd.str.count('english').sum()
        count_spanish_over_all = df_over_all.language_cd.str.count('spanish').sum()
        count_german_over_all = df_over_all.language_cd.str.count('german').sum()

        layout_language_distribution = html.Div([

            dcc.Graph(
                id='language_distribution',
                figure=go.Figure(
                    data=[
                        go.Bar(x=['Englisch', 'Spanisch', 'Deutsch'],
                               y=[count_english_over_all, count_spanish_over_all, count_german_over_all],
                               marker=dict(color=['#a3a3c2', '#a3a3c2', '#a3a3c2'],
                                           line=dict(color='#a3a3c2', width=2)),
                               name='Grundgesamtheit',
                               ),
                        go.Bar(x=['Englisch', 'Spanisch', 'Deutsch'],
                               y=[count_english_new, count_spanish_new, count_german_new],
                               marker=dict(color=['#248f24', '#47d147', '#99e699'],
                                           line=dict(color='#a3a3c2', width=2)),
                               name='Ausgewählte Kohorte',
                               )
                    ],

                    layout=go.Layout(
                        title='Verteilung nach Muttersprache',
                        showlegend=True,

                    )
                )
            )
        ])

        return layout_language_distribution
