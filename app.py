import dash
import dash_core_components as dcc
import dash_html_components as html

import database as db

app = dash.Dash(external_stylesheets=['style.css'])

app.layout = html.Div([
    html.Div([html.H1("Explorer")], className="Div1"),
    html.Div([html.H1("Ergebnisse")], className="Div2"),
    html.Div([html.H1("Query-Leiste")], className="Div3")
])

# Stop Flask Server Strg+C
if __name__ == '__main__':
    app.run_server(debug=True)
