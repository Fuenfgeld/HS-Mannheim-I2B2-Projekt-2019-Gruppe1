import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from config import database

# Benötigt für den Callback des Baums
from backend.tree import row_generator_level
from dash.dependencies import Output, Input, State

# imports der Klassen zur Anzeige der Seite
from frontend.app_layout import layout_banner
from frontend.app_layout import layout_query_bar
from frontend.app_layout import layout_navigation_bar
from frontend.app_layout import layout_results

from backend.query_bar_logic import query_bar

# Objekte zur Anzeige der Seite
bannerObject = layout_banner.layoutBanner()
queryBarObject = layout_query_bar.layoutQueryBar()
navigationBarObject = layout_navigation_bar.layoutNavigationBar()
resultsObject = layout_results.layoutResults()
queryBarLogicObject = query_bar.queryBar()

# Mockdaten
queryBarLogicObject.append_icd_list('ICD9:382.9')
#queryleiste.append_icd_list('ICD9:493')

result_icd = pd.read_sql(queryBarLogicObject.len_icd_aufruf(), con=database.engine)




app = dash.Dash(__name__)

# Visualisierung der Seite
app.layout = html.Div([

    bannerObject.layout_banner,

    navigationBarObject.layout_navigation,

    queryBarObject.layout_query_bar,

    resultsObject.show_results(result_icd)

])

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})


#CallBack des Baums
@app.callback(
    Output('selected', 'children'),
    [row_generator_level.secondLevelIDList[0]])
def update_div(secondLevelIDList):
    return

@app.callback(
    Output('output-container-button', 'children'),
    [Input('button', 'n_clicks')],
    [State('input-box', 'value')])
def update_output(n_clicks, value):
    if n_clicks == 1:
        queryBarLogicObject.name_list.clear()
    queryBarLogicObject.append_name_list(value)
    result = '{}'.format(
        queryBarLogicObject.print_name_list()
    )
    return result




if __name__ == "__main__":
    app.run_server(debug=True, port=5001)
