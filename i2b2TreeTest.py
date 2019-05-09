import dash
# import dash_core_components as dcc
import dash_html_components as html

import DB_Queries as db  # import from the file with the database query
# import plotly.graph_objs as go
import row_generator_tables as rg

columnNames = list(db.dfPat)

d = dash
app = d.Dash(
    external_stylesheets=['layout.css'],
    external_scripts=['Zdropdown.js'])

app.layout = html.Span(
    [html.Span('Patient dimension',
               className='caret'),
     html.Ul(
         rg.add_list_items(db.dfPat),
         className='nested'
     )]

)

if __name__ == '__main__':
    app.run_server(debug=True)
