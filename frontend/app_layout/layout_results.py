
import dash_html_components as html

from backend.result_logic import graph_sex_distribution
from backend.result_logic import layout_result_decimal

colors = {
    'background': '#ffffff',
    'text': '#111111'
}

sexObject = graph_sex_distribution.graphSexDistribution()
resultDecimalObject = layout_result_decimal.layoutResultDecimal()

class layoutResults:

    def show_results(self, df):

        layoutResults = html.Div([

            html.Div([

                resultDecimalObject.set_layout_decimal(df),

                sexObject.set_layout_sex_graph(df),


            ], className="DivErgebnis")

        ], className="row")

        return layoutResults
