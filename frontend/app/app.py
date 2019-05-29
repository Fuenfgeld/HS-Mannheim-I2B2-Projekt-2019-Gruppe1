import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from config import database

# Benötigt für den Callback des Baums
from backend.tree import row_generator_level
from dash.dependencies import Output

# imports der Klassen zur Anzeige der Seite
from frontend.app_layout import layout_banner
from frontend.app_layout import layout_query_bar
from frontend.app_layout import layout_navigation_bar
from frontend.app_layout import layout_graph

from backend.query_leiste.query_leiste import Queryleiste

# Objekte zur Anzeige der Seite
bannerObject = layout_banner.ShowBanner()
queryObject = layout_query_bar.ShowAbfrageleiste()
navigationObject = layout_navigation_bar.ShowNavigation()
graphObject = layout_graph.ShowGraph()
queryleiste = Queryleiste()

# Mockdaten
queryleiste.append_icd_list('ICD9:382.9')
queryleiste.append_icd_list('ICD9:493')

queryleiste.append_name_list("Rheumatic chorea without mention of heart involvement")
queryleiste.append_name_list("Rheumatic chorea with heart involvement")

result_icd = pd.read_sql(queryleiste.len_icd_aufruf(), con=database.engine)




app = dash.Dash(__name__)

# Visualisierung der Seite
app.layout = html.Div([

    bannerObject.layoutBanner,

    navigationObject.layoutNavigation,

    queryObject.showqueryleiste(queryleiste.name_list),

    graphObject.result_show(result_icd),

])

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})


# CallBack des Baums
@app.callback(
    Output('selected', 'children'),
    [row_generator_level.secondLevelIDList[0]])
def update_div(secondLevelIDList):
    return


if __name__ == "__main__":
    app.run_server(debug=True, port=5001)
