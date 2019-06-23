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
                    id='checklistSEX',
                    options=[{'label': 'Geschlecht', 'value': 'on'}],
                    values=['on'],
                    style={'display': 'inline-block'},
                    className='DivCheckbox'),
                dcc.Checklist(
                    id='checklistRace',
                    options=[{'label': 'Herkunft', 'value': 'on'}],
                    values=['on'],
                    style={'display': 'inline-block'},
                    className='DivCheckbox'),
                dcc.Checklist(
                    id='checklistAGE',
                    options=[{'label': 'Alter', 'value': 'on'}],
                    values=['on'],
                    style={'display': 'inline-block'},
                    className='DivCheckbox'),
                dcc.Checklist(
                    id='checklistIncome',
                    options=[{'label': 'Einkommen', 'value': 'on'}],
                    values=['off'],
                    style={'display': 'inline-block'},
                    className='DivCheckbox'),
                dcc.Checklist(
                    id='checklistLanguage',
                    options=[{'label': 'Sprache', 'value': 'on'}],
                    values=['off'],
                    style={'display': 'inline-block'},
                    className='DivCheckbox'),
                dcc.Checklist(
                    id='checklistBesides',
                    options=[{'label': 'Nebendia.', 'value': 'on'}],
                    style={'display': 'inline-block'},
                    values=['on'], className='DivCheckbox'),
            ],
                className='DivGesamtanzahlChecklist')

        layout_decimal = html.Div([
            html.Div(id='decimal', children=''),
        ], className='DivGesamtanzahl')

        layout_results = html.Div([
            html.Div(dcc.Graph(id='sex-distribution'),
                     style={'width': '29%', 'display': 'inline-block'},
                     className='DivSexDis'),
            html.Div(dcc.Graph(id='race-distribution'),
                     style={'width': '29%', 'display': 'inline-block'},
                     className='DivRaceDis'),
            html.Div(dcc.Graph(id='age-distribution'), style={'width': '42%', 'display': 'inline-block'}),
            html.Div(dcc.Graph(id='income-distribution'),
                     style={'display': 'inline-block'},

                     className='DivLanguageDis'),
            html.Div(dcc.Graph(id='language-distribution'),
                     style={'display': 'inline-block'},
                     className='DivLanguageDis'),
            html.Div(dcc.Graph(id='besides-diagnoses'))
        ], className="DivErgebnis", style={'width': '70%', 'display': 'inline-block'})