
import dash_html_components as html

from backend.result import show_geschlechterverteilung
from backend.result import ergebnis_dezimal

colors = {
    'background': '#ffffff',
    'text': '#111111'
}

geschlechtObject = show_geschlechterverteilung.Geschlechterverteilung()
ergDeziObject = ergebnis_dezimal.ErgebnisDezimal()


class ShowGraph():

    def result_show(self, df):

        layoutGraph = html.Div([

            html.Div([

                ergDeziObject.setlayoutdezimal(df),

                geschlechtObject.setlayoutgeschlecht(df),

                # herkunftObject.layoutHerkunft,

                # familienstandObject.layoutFamilienstand

            ], className="DivErgebnis")

        ], className="row")

        return layoutGraph
