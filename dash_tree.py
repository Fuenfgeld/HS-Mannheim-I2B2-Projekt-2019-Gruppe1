# import level_dictionary_faster
import dash
import dash_html_components as html

d = dash
app = d.Dash(__name__, external_stylesheets=['style.css'],
             external_scripts=['tree_dropdown.js'])

app.layout = html.Div(
    html.Div('Ah shit, here we go again.')
)

if __name__ == '__main__':
    app.run_server(debug=True)
