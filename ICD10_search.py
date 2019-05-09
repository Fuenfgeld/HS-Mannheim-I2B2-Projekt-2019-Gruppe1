import dash
import dash_html_components as html

import row_generator_ICD_levels as rgICD

d = dash
app = d.Dash(__name__,
             external_stylesheets=['layout.css'],
             external_scripts=['Zdropdown.js'])

app.layout = html.Span(
    [html.Span('ICD 10',
               className='caret'),
     html.Ul(
         rgICD.add_groundlevel(),
         className='nested'
     )]

)

if __name__ == '__main__':
    app.run_server(debug=True)
