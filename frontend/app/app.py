import dash
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

from backend.data_frame_logic import data_frame_logic
# imports für Logik
from backend.query_bar_logic import query_bar_logic
# imports der Klassen zur Anzeige der Seite
from frontend.app_layout import layout_banner
from frontend.app_layout import layout_navigation_bar
from frontend.app_layout import layout_query_bar
from frontend.app_layout import layout_results

# Benötigt für den Callback des Baums

# Objekte zur Anzeige der Seite
bannerObject = layout_banner.layoutBanner()
queryBarObject = layout_query_bar.layoutQueryBar()
navigationBarObject = layout_navigation_bar.layoutNavigationBar()
resultsObject = layout_results.layoutResults()
queryBarLogicObject = query_bar_logic.queryBar()

app = dash.Dash(__name__, external_stylesheets=
                ['https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css'],
                external_scripts=['https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.2/js/bootstrap.min.js',
                                  'http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js',
                                  
                                  ])


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




# # callback for the input field
# @app.callback(
#     Output('input-box', 'value'),
#     [Input('clear', 'n_clicks')],
# )
# def clear_input(n_clicks):
#     if n_clicks is not None:
#         return ''




##############################
# part to activate the working javascript returning

# @app.callback(
#     Output('input-box', 'className'),
#     [Input('javascript', 'event')])
# def myfun(x):
#     if x is not None:
#         string = str(x)[7:-12]
#         print(string)
#         return str(string)

####################################
# callback for the filling of the query bar
# @app.callback(
#     Output('input-box','className'),
#     [Input('input-box','value')]
# )
# def update_value(className):
#     print('Ill get this', className)
#     return className

@app.callback(
    Output('query-bar', 'children'),
    [Input('button', 'n_clicks')],
     [State('input-box', 'value')])
def update_output(n_clicks, value):
    print(n_clicks, value)
    if n_clicks is None:
        return 'Abfrageleiste'
    if n_clicks is not None or value is '':
        return 'Bitte Wert eingeben!'
    else:
        queryBarLogicObject.append_name_list(str(value).rstrip())
        result = '{}'.format(
            queryBarLogicObject.print_name_list())
        return result


# callback for the change of graphs
@app.callback(
    Output('decimal', 'children'),
    [Input('button', 'n_clicks')],
    [State('input-box', 'value')])
def update_output(n_clicks, value):
    if n_clicks is None or value is '':
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'decimal')
        count_patients = len(df_patients)
        return html.H5('Anzahl Patienten: ' + str(count_patients))
    if n_clicks is not None and (value is None or value is ''):
        raise PreventUpdate('No Changing!')


    else:
        df_code = data_frame_logic.generate_df_icd_code(queryBarLogicObject, str(value).rstrip())
        queryBarLogicObject.append_icd_list_decimal(df_code.loc[0].values[0])
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'decimal')
        count_patients = len(df_patients)
        return html.H5('Anzahl Patienten: ' + str(count_patients))


# another callback for the grap
@app.callback(
    Output('sex-distribution', 'figure'),
    [Input('button', 'n_clicks')],
    [State('input-box', 'className')])
def update_graph(n_clicks, value):
    if n_clicks is None:
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'sex_cd')
        count_male = df_patients.sex_cd.str.count('M').sum()
        count_female = df_patients.sex_cd.str.count('F').sum()
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
        df_code = data_frame_logic.generate_df_icd_code(queryBarLogicObject, value)
        queryBarLogicObject.append_icd_list_sex_cd(df_code.loc[0].values[0])
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'sex_cd')
        count_male = df_patients.sex_cd.str.count('M').sum()
        count_female = df_patients.sex_cd.str.count('F').sum()
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


@app.callback(
    Output('age-distribution', 'figure'),
    [Input('button', 'n_clicks')],
    [State('input-box', 'className')])
def update_graph(n_clicks, value):
    if n_clicks is None:
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'age_in_years_num')
        age_until_17 = (((df_patients['age_in_years_num']).ge(10)) & ((df_patients['age_in_years_num']).le(17))).sum()
        age_until_34 = (((df_patients['age_in_years_num']).ge(18)) & ((df_patients['age_in_years_num']).le(34))).sum()
        age_until_44 = (((df_patients['age_in_years_num']).ge(35)) & ((df_patients['age_in_years_num']).le(44))).sum()
        age_until_54 = (((df_patients['age_in_years_num']).ge(45)) & ((df_patients['age_in_years_num']).le(54))).sum()
        age_until_64 = (((df_patients['age_in_years_num']).ge(55)) & ((df_patients['age_in_years_num']).le(64))).sum()
        age_until_74 = (((df_patients['age_in_years_num']).ge(65)) & ((df_patients['age_in_years_num']).le(74))).sum()
        age_until_84 = (((df_patients['age_in_years_num']).ge(75)) & ((df_patients['age_in_years_num']).le(84))).sum()
        age_greater_85 = ((df_patients['age_in_years_num']).ge(85)).sum()
        return {
            'data': [go.Bar(
                x=['0-9', '10-17', '18-34', '35-44', '45-54', '55-64', '65-74', '75-84', '>=85'],
                y=[age_until_17, age_until_34, age_until_44, age_until_54, age_until_64, age_until_74, age_until_84,
                   age_greater_85],
                marker=dict(
                    color=['#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff'],
                    line=dict(color='#a3a3c2', width=2)),
            ),
            ],

            'layout': go.Layout(
                title='Altersverteilung',
            )
        }
    if n_clicks is not None and (value is None or value is ''):
        raise PreventUpdate('No Changing!')
    else:
        df_code = data_frame_logic.generate_df_icd_code(queryBarLogicObject, value)
        queryBarLogicObject.append_icd_list_age_in_years_num(df_code.loc[0].values[0])
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'age_in_years_num')
        age_until_17 = (((df_patients['age_in_years_num']).ge(10)) & ((df_patients['age_in_years_num']).le(17))).sum()
        age_until_34 = (((df_patients['age_in_years_num']).ge(18)) & ((df_patients['age_in_years_num']).le(34))).sum()
        age_until_44 = (((df_patients['age_in_years_num']).ge(35)) & ((df_patients['age_in_years_num']).le(44))).sum()
        age_until_54 = (((df_patients['age_in_years_num']).ge(45)) & ((df_patients['age_in_years_num']).le(54))).sum()
        age_until_64 = (((df_patients['age_in_years_num']).ge(55)) & ((df_patients['age_in_years_num']).le(64))).sum()
        age_until_74 = (((df_patients['age_in_years_num']).ge(65)) & ((df_patients['age_in_years_num']).le(74))).sum()
        age_until_84 = (((df_patients['age_in_years_num']).ge(75)) & ((df_patients['age_in_years_num']).le(84))).sum()
        age_greater_85 = ((df_patients['age_in_years_num']).ge(85)).sum()
        return {
            'data': [go.Bar(
                x=['0-9', '10-17', '18-34', '35-44', '45-54', '55-64', '65-74', '75-84', '>=85'],
                y=[age_until_17, age_until_34, age_until_44, age_until_54, age_until_64, age_until_74, age_until_84,
                   age_greater_85],
                marker=dict(
                    color=['#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff'],
                    line=dict(color='#a3a3c2', width=2)),
            ),
            ],

            'layout': go.Layout(
                title='Altersverteilung',
            )
        }


@app.callback(
    Output('language-distribution', 'figure'),
    [Input('button', 'n_clicks')],
    [State('input-box', 'value')])
def update_graph(n_clicks, value):
    if n_clicks is None:
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'language_cd')
        count_english = df_patients.language_cd.str.count('english').sum()
        count_spanish = df_patients.language_cd.str.count('spanish').sum()
        count_german = df_patients.language_cd.str.count('german').sum()
        return {
            'data': [go.Bar(
                x=['Englisch', 'Spanisch', 'Deutsch'],
                y=[count_english, count_spanish, count_german],
                marker=dict(color=['#4da6ff', '#4da6ff', '#4da6ff'],
                            line=dict(color='#a3a3c2', width=2)),
            ),
            ],

            'layout': go.Layout(
                title='Verteilung nach Muttersprache',
            )
        }
    if n_clicks is not None and (value is None or value is ''):
        raise PreventUpdate('No Changing!')
    else:
        df_code = data_frame_logic.generate_df_icd_code(queryBarLogicObject, value)
        queryBarLogicObject.append_icd_list_language_cd(df_code.loc[0].values[0])
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'language_cd')
        count_english = df_patients.language_cd.str.count('english').sum()
        count_spanish = df_patients.language_cd.str.count('spanish').sum()
        count_german = df_patients.language_cd.str.count('german').sum()
        return {
            'data': [go.Bar(
                x=['Englisch', 'Spanisch', 'Deutsch'],
                y=[count_english, count_spanish, count_german],
                marker=dict(color=['#4da6ff', '#4da6ff', '#4da6ff'],
                            line=dict(color='#a3a3c2', width=2)),
            ),
            ],

            'layout': go.Layout(
                title='Verteilung nach Muttersprache',
            )
        }


if __name__ == "__main__":
    app.run_server(debug=True, port=5001)
