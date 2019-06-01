# import level_dictionary_faster
import dash
import dash_html_components as html

d = dash
app = d.Dash(__name__, external_stylesheets=['style.css'],
             external_scripts=['tree_dropdown.js, bootstrap.js, jquery.js. jstree.js'])

app.layout = html.Div(
    [html.Div(className='container'),
     html.Div(id='jstree-tree')],
)

if __name__ == '__main__':
    app.run_server(debug=True)
