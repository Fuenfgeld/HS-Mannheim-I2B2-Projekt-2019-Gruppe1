import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import abfragenLogik.sqlGesamtanzahl as sqlGesamtanzahl
import tree.rowGenerator as rowGenerator
from dash.dependencies import Output

colors = {
    'background': '#ffffff',
    'text': '#111111'
}

sG = sqlGesamtanzahl.sqlGesamtanzahl()

app = dash.Dash(__name__,
                external_stylesheets=['layout.css'],
                external_scripts=['Zdropdown.js'])

app.layout = html.Div([
    html.Div([
        html.H2("medical deGREEN"),
        html.Img(src="/assets/LOGO.png")
    ], className="banner"),

    html.Div([dcc.Upload(
        id='upload-data',
        children=html.Div([
            html.H5('Drag and Drop - Abfrageleiste '),
        ]),
        style={
            'width': '98,5%',
            'height': '150px',
            'lineHeight': '60px',
            'borderWidth': '2px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ), ]
        , className='DivAbfrageleiste'),

    html.Div([
        html.Div([html.H5("Suchen")], className="DivSuchleiste"),
        html.Span([
            html.H5('ICD 10', className='caret'),
            html.Ul(rowGenerator.add_groundlevel(), className='nested'),
            html.Div(id='selected')])

    ], className="DivNavigation"),


    html.Div([

        html.Div([
            html.Div([html.H5(children="Anzahl Patienten: " + str(sG.gesamtanzahlPatienten()))], className='DivGesamtanzahl'),
            dcc.Graph(
                id="sex_distribution",
                figure={
                    'data': [
                        {'x': ['W'], 'y': [sG.gesamtanzahlGeschlecht("F")], 'type': 'bar', 'name': 'Weiblich'},
                        {'x': ['M'], 'y': [sG.gesamtanzahlGeschlecht("M")], 'type': 'bar', 'name': 'Männlich'},
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
            dcc.Graph(id='race_distribution',
                      figure=go.Figure(
                          data=[go.Pie(labels=['Afrikanisch', 'Europäisch', 'Asiatisch', 'Hispanisch', 'Indisch'],
                                       values=[sG.gesamtanzahlEthnie("black"), sG.gesamtanzahlEthnie("white"),
                                               sG.gesamtanzahlEthnie("asian"), sG.gesamtanzahlEthnie("hispanic"),
                                               sG.gesamtanzahlEthnie("indian")])],
                          layout=go.Layout(
                              title='Ethnische Verteilung')
                      )
            ),
            dcc.Graph(
                id='marital_status_distribution',
                figure={
                    'data': [
                        {'x': ['Alleinstehend'], 'y': [sG.gesamtanzahlFamilienstatus("single")], 'type': 'bar', 'name': 'Alleinstehend'},
                        {'x': ['Verheiratet'], 'y': [sG.gesamtanzahlFamilienstatus("married")], 'type': 'bar', 'name': 'Verheiratet'},
                        {'x': ['Geschieden'], 'y': [sG.gesamtanzahlFamilienstatus("divorced")], 'type': 'bar', 'name': 'Geschieden'},
                        {'x': ['Verwitwet'], 'y': [sG.gesamtanzahlFamilienstatus("widow")], 'type': 'bar', 'name': 'Verwitwet'},
                    ],
                    'layout': {
                        'title': 'Verteilung nach Familienstatus',
                        'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font': {
                            'color': colors['text']
                        }
                    }
                }
            )

        ], className="DivErgebnis")

    ], className="row")
])

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

@app.callback(
    Output('selected', 'children'),
    [rowGenerator.secondLevelIDList[0]])
def update_div(secondLevelIDList):
    return

if __name__ == "__main__":
    app.run_server(debug=True, port=5001)
