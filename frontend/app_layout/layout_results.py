import dash_core_components as dcc
import dash_html_components as html

from backend.result_logic import graph_sex_distribution
from backend.result_logic import layout_result_decimal
from backend.result_logic import graph_language_distribution

colors = {
    'background': '#ffffff',
    'text': '#111111'
}

# sexObject = graph_sex_distribution.graphSexDistribution()
# languageObject = graph_language_distribution.graphLanguageDistribution()
# resultDecimalObject = layout_result_decimal.layoutResultDecimal()


class layoutResults:

        layout_results = html.Div([
                dcc.Graph(id='sex-distribution')
            ], className="DivErgebnis")



