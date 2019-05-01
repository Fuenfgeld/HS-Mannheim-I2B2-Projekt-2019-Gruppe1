import dash   # main thing we need to import (uses plotly for visualization)
import dash_html_components as html     # components for the use of html elements
import dash_core_components as dcc      # components for the use of graphs
import pandas as pd                     # for the ability to read csv files
import plotly.graph_objs as go
from dash.dependencies import Output, Input


d = dash   # shortened definition for the later use of app.run
app = d.Dash()

demoData = pd.read_csv('Demodata_patient.csv', na_values={'""', ' '})
colors = {
    'background': 'white',    # just to be sure, put a whitespace after every , ; and # to avoid errors
    'text': 'black'           # and 2 whitespaces after the code to avoid errors
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[   # now we kinda make the whole DOM
                                                                                    # tree with the definition of
                                                                                    # its children etc.
    html.H1(                        # notice how the elements H1 (capital first) and others are the same as in HTML
        children='Patients divided by relationship status',     # same effect as writing plain text after <h1> in HTML
                                                                # as it is the child of h1 (see below)
                                                                # <h1> Hello Dash </h1>

        style={                     # style similar to HTML/CSS with 'attribute':'value', then no ;, just a comma
            'textAlign': 'center',  # if you need to give more than one attributes
            'color': 'black'
        }
    ),
    html.Div(
        # children='Hello again',
        # style={
        #     'text-align': 'right',
        #     'color': 'blue'
        # }
    ),
    dcc.Graph(      # with dcc, graphs can be created with a lot of attributes each separated by a comma

        id='bar graph',     # the id it can be referenced with

        figure={    # the definition of this will be a figure with the following properties

            'data': [   # data can contain multiple graphs at once, here defined in a list of graphs
                # go.Scatter(
                #     x=demoData[demoData['race'] == i]['age'],   # i to be able to make it interactive and choose
                #     y=demoData[demoData['race'] == i]['nation'],
                #     text=demoData[demoData['race'] == i]['sex'],
                #     mode='markers',     # In order to make sure the plot is a scatter plot
                #                         we pass a "mode" attribute and set it as markers
                #     opacity=0.8,
                #     marker={    # how big are the markers and which color
                #         'size': 15,
                #         'line': {'width': 0.5, 'color': 'blue'}
                #     },
                #     name=i
                #
                # ) for i in demoData.race.unique() # for I in each unique thing in the column race

                # go.Bar(
                #     x=['F', 'M'],
                #     y=[len(demoData[(demoData['relationship'] == 'divorced') & (demoData['sex'] == 'F')]),
                #        len(demoData[(demoData['relationship'] == 'divorced') & (demoData['sex'] == 'M')])],
                #     name='divorced by sex'
                #     ),
                # go.Bar(
                #     x=['F', 'M'],
                #     y=[len(demoData[(demoData['relationship'] == 'married') & (demoData['sex'] == 'F')]),
                #        len(demoData[(demoData['relationship'] == 'married') & (demoData['sex'] == 'M')])],
                #     name='married by sex'
                #     ),
                # go.Bar(
                #     x=['F', 'M'],
                #     y=[len(demoData[(demoData['relationship'] == 'single') & (demoData['sex'] == 'F')]),
                #        len(demoData[(demoData['relationship'] == 'single') & (demoData['sex'] == 'M')])],
                #     name='single by sex'
                #     ),
                # go.Bar(
                #     x=['F', 'M'],
                #     y=[len(demoData[(demoData['relationship'] == 'widow') & (demoData['sex'] == 'F')]),
                #        len(demoData[(demoData['relationship'] == 'widow') & (demoData['sex'] == 'M')])],
                #     name='widowed by sex'
                #     ),

            ],
            'layout': go.Layout(  # definition of how the graphs will look like
                hovermode='closest',  # what to hover on
                barmode='stack'
            )
        }
    ),
    dcc.Dropdown(
        id='relationship dropdown',
        options=[
            {'label': i, 'value': i} for i in demoData['relationship'].unique()
            ],

    ),


])


@app.callback(  # this part defines what to do if something changes
    Output('bar graph', 'figure'),
    [Input('relationship dropdown', 'value')])
def update_graph(relationship_choice):  # this is the function that is called every time something changes with the
    # variable relationship choice that is passed down from the input in the order
    # in which the inputs were mentioned

    relationship = demoData['relationship']

    return{
        'data': [go.Bar(
            x=['F', 'M'],
            y=[len(demoData[(relationship == relationship_choice) & (demoData['sex'] == 'F')]),
               len(demoData[(relationship == relationship_choice) & (demoData['sex'] == 'M')])]
            #  has to be exactly like the previous graph

        )],
        'layout': go.Layout(  # definition of how the graphs will look like
            hovermode='closest',  # what to hover on
            barmode='stack'
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
