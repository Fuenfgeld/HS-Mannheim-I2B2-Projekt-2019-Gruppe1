import dash_core_components as dcc
import dash_html_components as html

colors = {
    'background': '#ffffff',
    'text': '#111111'
}

# sexObject = graph_sex_distribution.graphSexDistribution()
# languageObject = graph_language_distribution.graphLanguageDistribution()
# resultDecimalObject = layout_result_decimal.layoutResultDecimal()

class layoutResults:
    layout_results = html.Div([
        html.Div(id='decimal', children='', className='DivGesamtanzahl'),
        dcc.Graph(id='sex-distribution'),
        dcc.Graph(id='age-distribution'),
        dcc.Graph(id='language-distribution')
    ], className="DivErgebnis")
