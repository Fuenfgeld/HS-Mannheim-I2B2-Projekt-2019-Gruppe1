import dash_core_components as dcc
import dash_html_components as html
from backend.result_logic import result_merge

colors = {
    'background': '#ffffff',
    'text': '#111111'
}


class graphSexDistribution():

    def __init__(self):
        self.count_male = 82
        self.count_female = 52

    def set_layout_sex_graph(self, df):
        if df is not None:
            dfNew = result_merge.merge_two_df(df)
            self.count_male = dfNew.sex_cd.str.count('M').sum()
            self.count_female = dfNew.sex_cd.str.count('F').sum()

        layoutSexDistribution = html.Div([

            dcc.Graph(
                id="sex_distribution",
                figure={
                    'data': [
                        {'x': ['W'], 'y': [self.count_female], 'type': 'bar', 'name': 'Frauen'},
                        {'x': ['M'], 'y': [self.count_male], 'type': 'bar', 'name': 'Männlich'},
                    ],
                    'layout': {
                        'title': 'Geschlechterverteilung',
                        'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font': {
                            'color': colors['text']
                        }
                    }
                }
            ),

        ])

        return layoutSexDistribution
