import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from backend.result_logic import result_merge

class graphSexDistribution():

    def set_layout_sex_graph(self, df):
        if df is None:
            dfAll = result_merge.generate_df_sex_cd_patient_dimension()
            count_male = dfAll.sex_cd.str.count('M').sum()
            count_female = dfAll.sex_cd.str.count('F').sum()

        else:
            dfNew = result_merge.merge_two_df(df, 'sex_cd')
            count_male = dfNew.sex_cd.str.count('M').sum()
            count_female = dfNew.sex_cd.str.count('F').sum()

        layoutSexDistribution = html.Div([

            dcc.Graph(
                id="sex_distribution",
                figure=go.Figure(
                    data=[go.Pie(labels=['Weiblich', 'Männlich'],
                                 values=[count_female,
                                         count_male],
                                 marker=dict(colors=['#d0d0e1', '#85e085'],
                                             line=dict(color='#a3a3c2', width=2)),
                                 textfont={'size': 15},
                                 textinfo='value'
                                 )
                          ],

                    layout=go.Layout(
                        title='Geschlechterverteilung'
                    )
                )
            )
        ])

        return layoutSexDistribution
