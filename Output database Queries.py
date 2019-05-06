import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import DB_Test as db  # import from the file with the database query

d = dash
app = d.Dash()

app.layout = html.Div(children=[
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
    )
]
)

if __name__ == '__main__':
    app.run_server(debug=True)
