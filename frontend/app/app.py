import dash
import dash_html_components as html
from dash.exceptions import PreventUpdate
from dash.dependencies import Output, Input, State
import plotly.graph_objs as go
import pandas as pd

# Benötigt für den Callback des Baums
from deprecated import row_generator_level

# imports der Klassen zur Anzeige der Seite
from frontend.app_layout import layout_banner
from frontend.app_layout import layout_query_bar
from frontend.app_layout import layout_navigation_bar
from frontend.app_layout import layout_results

# imports für Logik und Datenbankanbindung
from backend.query_bar_logic import query_bar_logic
from backend.result_logic import result_merge
from backend.data_frame_logic import data_frame_logic
from config import database


# Objekte zur Anzeige der Seite
bannerObject = layout_banner.layoutBanner()
queryBarObject = layout_query_bar.layoutQueryBar()
navigationBarObject = layout_navigation_bar.layoutNavigationBar()
resultsObject = layout_results.layoutResults()
queryBarLogicObject = query_bar_logic.queryBar()

app = dash.Dash(__name__)

# Visualisierung der Seite
app.layout = html.Div([

    bannerObject.layout_banner,

    navigationBarObject.layout_navigation,

    queryBarObject.layout_query_bar,

    resultsObject.layout_results

])

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})


# #CallBack des Baums
# @app.callback(
#     Output('selected', 'children'),
#     [row_generator_level.secondLevelIDList[0]])
# def update_div(secondLevelIDList):
#     return

@app.callback(
    Output('query-bar', 'children'),
    [Input('button', 'n_clicks')],
    [State('input-box', 'value')])
def update_output(n_clicks, value):
    if n_clicks is None:
        return 'Abfrageleiste'
    if n_clicks is not None and (value is None or value is ''):
        return 'Bitte Wert eingeben!'
    else:
        queryBarLogicObject.append_name_list(value)
        result = '{}'.format(
            queryBarLogicObject.print_name_list())
        return result

@app.callback(
    Output('sex-distribution', 'figure'),
    [Input('button', 'n_clicks')],
    [State('input-box', 'value')])
def update_graph(n_clicks, value):
    if n_clicks is None:
        queryBarLogicObject.delete_icd_list_items()
        dfPatients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'sex_cd')
        count_male = dfPatients.sex_cd.str.count('M').sum()
        count_female = dfPatients.sex_cd.str.count('F').sum()
        return {
            'data': [go.Pie(
                labels=['Weiblich', 'Männlich'],
                values=[count_female,
                        count_male],
                marker=dict(colors=['#d0d0e1', '#4da6ff'],
                            line=dict(color='#a3a3c2', width=2)),
                textfont={'size': 15},
                textinfo='value'
            )
            ],

            'layout': go.Layout(
                title='Geschlechterverteilung'
            )
        }
    if n_clicks is not None and (value is None or value is ''):
        raise PreventUpdate('No Changing!')
    else:
        dfCode = data_frame_logic.generate_df_icd_code(queryBarLogicObject, value)
        queryBarLogicObject.append_icd_list(dfCode.loc[0].values[0])
        dfPatients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'sex_cd')
        count_male = dfPatients.sex_cd.str.count('M').sum()
        count_female = dfPatients.sex_cd.str.count('F').sum()
        return {
            'data': [go.Pie(
                labels=['Weiblich', 'Männlich'],
                values=[count_female,
                        count_male],
                marker=dict(colors=['#d0d0e1', '#4da6ff'],
                            line=dict(color='#a3a3c2', width=2)),
                textfont={'size': 15},
                textinfo='value'
            )
            ],

            'layout': go.Layout(
                title='Geschlechterverteilung'
            )
        }


if __name__ == "__main__":
    app.run_server(debug=True, port=5001)
