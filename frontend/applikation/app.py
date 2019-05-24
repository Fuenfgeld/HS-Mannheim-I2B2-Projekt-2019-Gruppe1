import dash
import dash_core_components as dcc
import dash_html_components as html

#Benötigt für den Callback des Baums
from backend.baum import row_generator
from dash.dependencies import Output

#imports der Klassen zur Anzeige der Seite
from frontend.applikation import show_banner
from frontend.applikation import query_bar
from frontend.applikation import navigation_bar
from frontend.applikation import show_graph
from frontend.applikation import show_geschlechterverteilung


#Objekte zur Anzeige der Seite
bannerObject = show_banner.ShowBanner()
queryObject = query_bar.ShowAbfrageleiste()
navigationObject = navigation_bar.ShowNavigation()
graphObject = show_graph.ShowGraph()


sexObject = show_geschlechterverteilung.Geschlechterverteilung()


app = dash.Dash(__name__)

#Visualisierung der Seite
app.layout = html.Div([

    bannerObject.layoutBanner,

    queryObject.layoutQuery,

    navigationObject.layoutNavigation,

    graphObject.layoutGraph,


])

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

#CallBack des Baums
@app.callback(
    Output('selected', 'children'),
    [row_generator.secondLevelIDList[0]])
def update_div(secondLevelIDList):
    return

if __name__ == "__main__":
    app.run_server(debug=True, port=5001)
