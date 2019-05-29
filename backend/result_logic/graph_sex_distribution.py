import dash_core_components as dcc
import dash_html_components as html
from backend.result_logic import result_merge

colors = {
    'background': '#ffffff',
    'text': '#111111'
}


class graphSexDistribution():

    def set_layout_sex_graph(self, df):
        dfnew = result_merge.merge_two_df(df)

        layoutSexDistribution = html.Div([

            dcc.Graph(
                id="sex_distribution",
                figure={
                    'data': [
                        {'x': ['W'], 'y': [dfnew.sex_cd.str.count('F').sum()], 'type': 'bar', 'name': 'Frauen'},
                        {'x': ['M'], 'y': [dfnew.sex_cd.str.count('M').sum()], 'type': 'bar', 'name': 'Männlich'},
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
