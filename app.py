import dash
import dash_core_components as dcc
import dash_html_components as html

import database as db


app = dash.Dash(external_stylesheets=['style.css'])


#app.layout = html.Div([
#    html.Div([
#        html.H1("Query-Leiste"),
#    ], className="Qu"),
#
#    html.Div([
#        html.H1("Explorer"),
#    ], className="Ex"),
#
#    html.Div([
#        html.H1("Ergebnisse")
#    ], className="Er"),
#])

app.layout = html.Div([
html.Div(["Div1"],className="Div1", style={"position": "absolute", "width": "50%", "height": "80%", "z-index": 1, "left": "0%", "top":"20%", "border":"solid"}),
html.Div(["Div2"],className="Div2", style={"position": "absolute", "width": "50%", "height": "80%", "z-index": 1, "left": "50%", "top":"20%", "border":"solid"}),
html.Div(["Div3"],className="Div3", style={"position": "absolute", "width": "100%", "height": "20%", "z-index": 2, "left": "0%", "top": "0%", "border":"solid"})
])





# Stop Flask Server Strg+C
if __name__ == '__main__':
    app.run_server(debug=True)
