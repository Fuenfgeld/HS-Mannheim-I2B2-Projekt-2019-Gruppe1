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
                    values=['on'], className='DivSexRaceCheckbox'),
                dcc.Checklist(
                    id='checklistRace',
                    options=[{'label': 'Herkunft', 'value': 'on'}],
                    values=['on'], className='DivSexRaceCheckbox'),
                dcc.Checklist(
                    id='checklistAGE',
                    options=[{'label': 'Alter', 'value': 'on'}],
                    values=['on'], className='DivAgeCheckbox'),
                dcc.Checklist(
                    id='checklistIncome',
                    options=[{'label': 'Einkommen', 'value': 'on'}],
                    values=['off'], className='DivIncomeCheckbox'),
                dcc.Checklist(
                    id='checklistLanguage',
                    options=[{'label': 'Sprache', 'value': 'on'}],
                    values=['off'], className='DivLanguCheckbox'),
                dcc.Checklist(
                    id='checklistBesides',
                    options=[{'label': 'Nebendia.', 'value': 'on'}],
                    values=['on'], className='DivBesideCheckbox'),
            ], className='DivGesamtanzahlChecklist')

        layout_decimal = html.Div([
            html.Div(id='decimal', children=''),
        ], className='DivGesamtanzahl')

        layout_results = html.Div([

            dcc.Graph(id='race-distribution', className='DivRaceDis'),
            dcc.Graph(id='sex-distribution', className='DivSexDis'),
            dcc.Graph(id='age-distribution', className='DivAgeDis'),
            dcc.Graph(id='income-distribution', style={'display': 'none'}),
            dcc.Graph(id='language-distribution', style={'display': 'none'}),
            #dcc.Graph(id='besides-diagnoses')
        ], className="DivErgebnis")
