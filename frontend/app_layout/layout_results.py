import dash_core_components as dcc
import dash_html_components as html

colors = {
    'background': '#ffffff',
    'text': '#111111'
}


class layoutResults:
    layout_results = html.Div([
        html.Div(id='decimal', children='', className='DivGesamtanzahl'),
        dcc.Graph(id='race-distribution', className='DivRaceDis'),
        dcc.Graph(id='sex-distribution', className='DivSexDis'),
        dcc.Graph(id='age-distribution', className='DivAgeDis'),
        # dcc.Graph(id='language-distribution')
    ], className="DivErgebnis")
