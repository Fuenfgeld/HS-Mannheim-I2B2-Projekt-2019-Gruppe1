
import dash_html_components as html

from backend.result_logic import graph_sex_distribution
from backend.result_logic import laylout_result_decimal

colors = {
    'background': '#ffffff',
    'text': '#111111'
}

sexObject = graph_sex_distribution.graphSexDistribution()
resultDecimalObject = laylout_result_decimal.ErgebnisDezimal()


class layoutGraph:

    def result_show(self, df):

        layoutGraph = html.Div([

            html.Div([

                resultDecimalObject.set_layout_decimal(df),

                sexObject.set_layout_sex_graph(df),

                # herkunftObject.layoutHerkunft,

                # familienstandObject.layoutFamilienstand

            ], className="DivErgebnis")

        ], className="row")

        return layoutGraph
