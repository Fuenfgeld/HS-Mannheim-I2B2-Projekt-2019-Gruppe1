import dash
import dash_html_components as html

from frontend.applikation import show_geschlechterverteilung
from frontend.applikation import ergebnis_dezimal
from frontend.applikation import verteilung_herkunft
from frontend.applikation import show_familienstand

colors = {
    'background': '#ffffff',
    'text': '#111111'
}

geschlechtObject = show_geschlechterverteilung.Geschlechterverteilung()
ergDeziObject = ergebnis_dezimal.ErgebnisDezimal()
herkunftObject = verteilung_herkunft.Herkunft()
familienstandObject = show_familienstand.Familienstand()

class ShowGraph():

    app = dash.Dash(__name__)

    layoutGraph = app.layout

    layoutGraph = html.Div([

        html.Div([

            ergDeziObject.layoutErgebnisDezimal,

            geschlechtObject.layoutGeschlechterverteilung,

            herkunftObject.layoutHerkunft,

            familienstandObject.layoutFamilienstand

        ], className="DivErgebnis")

    ], className="row")
