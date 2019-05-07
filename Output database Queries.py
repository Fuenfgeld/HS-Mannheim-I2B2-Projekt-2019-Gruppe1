import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import DB_Test as db  # import from the file with the database query

d = dash
app = d.Dash(
    external_stylesheets=['layout.css'],
    external_scripts=['Zdropdown.js'])

# app.css.append_css()

app.layout = html.Div([
    html.H1(
        children="let's do this"
    ),

    dcc.Graph(
        id="data visualisation",
        figure={
            'data': [
                go.Histogram(
                    x=db.df["length_of_stay"]
                ),
            ],
            'layout': go.Layout(
                title='length of stay',
                xaxis={'title': 'length in days'},
                yaxis={'title': 'amount of patients'}
            )
        }
    ),
    html.Ul(
        [
            html.Span(
                className='caret',
                children='Beverages'
            ),
            html.Ul(
                [
                    html.Div('Coffee'),
                    html.Div('Water'),
                    html.Li(
                        [
                            html.Span(
                                'Tea',
                                className='caret',
                            ),
                            html.Ul(
                                [
                                    html.Div('White Tea'),
                                    html.Div('Black Tea'),
                                    html.Li(
                                        [
                                            html.Span(
                                                'Green Tea',
                                                className='caret'

                                            ),

                                            html.Ul(
                                                [
                                                    html.Div('Sencha'),
                                                    html.Div('Spi Lon Chun'),
                                                    html.Div('Gyokuro'),
                                                    html.Div('Matcha'),
                                                ],

                                                className='nested'

                                            )
                                        ]
                                    )
                                ],
                                className='nested',

                            )
                        ]
                    )
                ],
                className='nested',
            )
        ],
        id='tree_view_test',
    ),
    html.Link(
        href='Zdropdown.css',
        rel='stylesheet'
    )
],
    # gdc.Import(src="Zdropdown.js")
)

if __name__ == '__main__':
    # app.layout += []
    app.run_server(debug=True)
