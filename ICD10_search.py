import dash
import dash_html_components as html
from dash.dependencies import Output

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
     ),
     html.Div(id='selected')]

)


@app.callback(
    Output('selected', 'children'),
    [rgICD.secondLevelIDList[0]])
def update_div(secondLevelIDList):
    return f'you have selected the code{secondLevelIDList}'.format()


if __name__ == '__main__':
    app.run_server(debug=True)
