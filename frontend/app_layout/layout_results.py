import dash_core_components as dcc
import dash_html_components as html

colors = {
    'background': '#ffffff',
    'text': '#111111'
}


class layoutResults:
    layout_checkout = \
        html.Div(children=[
            dcc.Checklist(
                id='checklistAGE',
                options=[{'label': 'Age', 'value': 'on'}],
                values=['on'],
                style={'display': 'inline-block'},
                className='DivCheckbox'),
            dcc.Checklist(
                id='checklistSEX',
                options=[{'label': 'Gender', 'value': 'on'}],
                values=['on'],
                style={'display': 'inline-block'},
                className='DivCheckbox'),
            dcc.Checklist(
                id='checklistBesides',
                options=[{'label': 'Common dis./Secondary diag.', 'value': 'on'}],
                style={'display': 'inline-block'},
                values=['on'],
                className='DivCheckbox'),
            dcc.Checklist(
                id='checklistIncome',
                options=[{'label': 'Income', 'value': 'on'}],
                values=['off'],
                style={'display': 'inline-block'},
                className='DivCheckbox'),
            dcc.Checklist(
                id='checklistLanguage',
                options=[{'label': 'Language', 'value': 'on'}],
                values=['off'],
                style={'display': 'inline-block'},
                className='DivCheckbox'),
            dcc.Checklist(
                id='checklistRace',
                options=[{'label': 'Ethnic origin', 'value': 'on'}],
                values=['off'],
                style={'display': 'inline-block'},
                className='DivCheckbox'),
        ],
            className='DivGesamtanzahlChecklist')

    layout_decimal = html.Div([
        html.Div(id='decimal', children=''),
    ], className='DivGesamtanzahl')

    layout_results = html.Div(
        [html.Div(dcc.Graph(id='age-distribution'),
                  style={'width': '61.5%', 'display': 'inline-block', 'border-right': '1px solid',
                         'border-right-color': 'lightgrey'}),
         html.Div(dcc.Graph(id='sex-distribution'),
                  style={'width': '38%', 'display': 'inline-block', 'border-left': '1px solid',
                         'border-left-color': 'lightgrey'}),
         html.Div(dcc.Graph(id='besides-diagnoses')),
         html.Div(dcc.Graph(id='income-distribution'),
                  style={'width': '49.5%', 'border-right': '1px solid', 'border-right-color': 'lightgrey',
                         'display': 'inline-block'}),
         html.Div(dcc.Graph(id='language-distribution'), style={'width': '50%', 'display': 'inline-block'}),
         html.Div(dcc.Graph(id='race-distribution')),
         ], className="DivErgebnis")
