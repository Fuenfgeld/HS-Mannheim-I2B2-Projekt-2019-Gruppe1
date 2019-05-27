import dash
import dash_core_components as dcc
import dash_html_components as html
from backend.result import ergebnis_merge


colors = {
    'background': '#ffffff',
    'text': '#111111'
}


class Geschlechterverteilung():
    app = dash.Dash(__name__)

    # gesamtAnzahl = gesamt_anzahl.GesamtAnzahl()

    layoutGeschlechterverteilung = app.layout

    def setlayoutgeschlecht(self, df):

        dfnew = ergebnis_merge.mergezweidf(df)

        layoutGeschlechterverteilung = html.Div([



            dcc.Graph(
                id="sex_distribution",
                figure={
                    'data': [
                        {'x': ['W'], 'y': [dfnew.sex_cd.str.count('F').sum()], 'type': 'bar', 'name': 'Frauen'},
                        {'x': ['M'], 'y': [dfnew.sex_cd.str.count('M').sum()], 'type': 'bar', 'name': 'Männlich'},
                    ],
                    'layout': {
                        'title': 'Geschlechterverteilung',
                        'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font': {
                            'color': colors['text']
                        }
                    }
                }
            ),

        ])

        return layoutGeschlechterverteilung
