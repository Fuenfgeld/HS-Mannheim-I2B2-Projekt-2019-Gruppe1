import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from config import database

# Benötigt für den Callback des Baums
from backend.tree import row_generator_level
from dash.dependencies import Output

# imports der Klassen zur Anzeige der Seite
from frontend.app_logic import show_banner
from frontend.app_logic import query_bar
from frontend.app_logic import navigation_bar
from frontend.app_logic import show_graph
from backend.result import show_geschlechterverteilung

from backend.query_leiste.query_leiste import Queryleiste

# Objekte zur Anzeige der Seite
bannerObject = show_banner.ShowBanner()
queryObject = query_bar.ShowAbfrageleiste()
navigationObject = navigation_bar.ShowNavigation()
graphObject = show_graph.ShowGraph()
queryleiste = Queryleiste()

sexObject = show_geschlechterverteilung.Geschlechterverteilung()

queryleiste.append_icd_list('ICD9:008.8')
#queryleiste.append_icd_list('ICD9:008.8')

result_icd = pd.read_sql(queryleiste.len_icd_aufruf(), con=database.engine)
print(result_icd)

app = dash.Dash(__name__)

# Visualisierung der Seite
app.layout = html.Div([

    bannerObject.layoutBanner,

    navigationObject.layoutNavigation,

    queryObject.layoutQuery,

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
