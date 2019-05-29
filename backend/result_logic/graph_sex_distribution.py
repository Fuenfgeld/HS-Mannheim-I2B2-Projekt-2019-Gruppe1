import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from backend.result_logic import result_merge

colors = {
    'background': '#ffffff',
    'text': '#111111'
}


class graphSexDistribution():

    def set_layout_sex_graph(self, df):
        dfNew = result_merge.merge_two_df(df)
        count_male = dfNew.sex_cd.str.count('M').sum()
        count_female = dfNew.sex_cd.str.count('F').sum()

        layoutSexDistribution = html.Div([

            dcc.Graph(
                id="sex_distribution",
                figure=go.Figure(
                    data=[go.Pie(labels=['Weiblich', 'Männlich'],
                                 values=[count_female,
                                         count_male])],
                    layout=go.Layout(
                        title='Geschlechterverteilung'
                    )
                )
            )
        ])

        return layoutSexDistribution
