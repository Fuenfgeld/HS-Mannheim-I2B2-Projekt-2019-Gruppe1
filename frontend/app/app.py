import dash
import dash_html_components as html
from dash.exceptions import PreventUpdate
from dash.dependencies import Output, Input, State

# imports der Klassen zur Anzeige der Seite
from frontend.app_layout import layout_banner
from frontend.app_layout import layout_query_bar
from frontend.app_layout import layout_navigation_bar
from frontend.app_layout import layout_results

# imports für Logik und Datenbankanbindung
from backend.query_bar_logic import query_bar_logic
from backend.data_frame_logic import data_frame_logic
from backend.graph_logic import age_graph_builder
from backend.graph_logic import sex_graph_builder
from backend.graph_logic import race_graph_builder
from backend.graph_logic import language_graph_builder

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

    queryBarObject.layout_delete_button,

    queryBarObject.layout_criteria_one,

    queryBarObject.layout_connection1_button,

    queryBarObject.layout_criteria_two,

    queryBarObject.layout_query_bar,

    resultsObject.layout_results

])

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})


# @app.callback(
#     Output('query-bar', 'children'),
#     [Input('clicked-button', 'children')],
#     [State('input-box', 'value')]
# )
# def update_query_bar(clicked, value):
#     last_clicked = clicked[-3:]
#     if last_clicked == 'nan':
#         return 'Abfrageleiste'
#     if last_clicked == 'del' or (last_clicked == 'del' and (value is None or value is '')):
#         queryBarLogicObject.name_list.clear()
#         return 'Abfrageleiste'
#     if last_clicked != 'nan' and (value is None or value is ''):
#         return 'Bitte Wert eingeben!'
#     if last_clicked == 'add':
#         queryBarLogicObject.append_name_list(value)
#         result = '{}'.format(
#             queryBarLogicObject.print_name_list())
#         return result

@app.callback([
    Output('criteria1-div', 'hidden'),
    Output('criteria1-div', 'children'),
    Output('criteria2-div', 'hidden'),
    Output('criteria2-div', 'children')],
    [Input('clicked-button', 'children')],
    [State('input-box', 'value')]
)
def update_criteria1_div(clicked, value):
    last_clicked = clicked[-3:]
    if last_clicked == 'nan':
        return True, '', True, ''
    if last_clicked == 'del' or (last_clicked == 'del' and (value is None or value is '')):
        queryBarLogicObject.name_list.clear()
        return True, '', True, ''
    if last_clicked != 'nan' and (value is None or value is ''):
        return True, '', True, ''
    if last_clicked == 'add':
        if len(queryBarLogicObject.name_list) == 0:
            queryBarLogicObject.append_name_list(value)
            return False, value, True, ''
        if len(queryBarLogicObject.name_list) == 1:
            queryBarLogicObject.append_name_list(value)
            return False, queryBarLogicObject.name_list[0], False, value
        else:
            raise PreventUpdate('No Changing!')


# @app.callback([
#     Output('criteria2-div', 'hidden'),
#     Output('criteria2-div', 'children')],
#     [Input('clicked-button', 'children')],
#     [State('input-box', 'value')]
# )
# def update_criteria1_div(clicked, value):
#     last_clicked = clicked[-3:]
#     if last_clicked == 'nan':
#         return True, ''
#     if last_clicked == 'del' or (last_clicked == 'del' and (value is None or value is '')):
#         queryBarLogicObject.name_list.clear()
#         return True, ''
#     if last_clicked != 'nan' and (value is None or value is ''):
#         return True, ''
#     if last_clicked == 'add':
#         if len(queryBarLogicObject.name_list) == 1:
#             print(queryBarLogicObject.name_list)
#             queryBarLogicObject.append_name_list(value)
#             result = '{}'.format(value)
#             return False, result
#         else:
#             raise PreventUpdate('No Changing!')


@app.callback(

    Output('decimal', 'children'),
    [Input('clicked-button', 'children')],
    [State('input-box', 'value')]
)
def update_decimal(clicked, value):
    last_clicked = clicked[-3:]
    if last_clicked == 'nan' or last_clicked == 'del':
        if last_clicked == 'del' or (last_clicked == 'del' and (value is None or value is '')):
            queryBarLogicObject.icd_list_decimal.clear()
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'decimal')
        count_patients = len(df_patients)
        return html.H5('Anzahl Patienten: ' + str(count_patients))
    if last_clicked != 'nan' and (value is None or value is ''):
        raise PreventUpdate('No Changing!')
    if last_clicked == 'add':
        df_code = data_frame_logic.generate_df_icd_code(queryBarLogicObject, value)
        queryBarLogicObject.append_icd_list_decimal(df_code.loc[0].values[0])
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'decimal')
        count_patients = len(df_patients)
        return html.H5('Anzahl Patienten: ' + str(count_patients))


@app.callback(
    Output('sex-distribution', 'figure'),
    [Input('clicked-button', 'children')],
    [State('input-box', 'value')]
)
def update_figure_sex_distribution(clicked, value):
    last_clicked = clicked[-3:]
    if last_clicked == 'nan' or last_clicked == 'del':
        if last_clicked == 'del' or (last_clicked == 'del' and (value is None or value is '')):
            queryBarLogicObject.icd_list_sex_cd.clear()
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'sex_cd')
        return sex_graph_builder.build_sex_graph(df_patients)
    if last_clicked != 'nan' and (value is None or value is ''):
        raise PreventUpdate('No Changing!')
    if last_clicked == 'add':
        df_code = data_frame_logic.generate_df_icd_code(queryBarLogicObject, value)
        queryBarLogicObject.append_icd_list_sex_cd(df_code.loc[0].values[0])
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'sex_cd')
        return sex_graph_builder.build_sex_graph(df_patients)


@app.callback(
    Output('race-distribution', 'figure'),
    [Input('clicked-button', 'children')],
    [State('input-box', 'value')]
)
def update_figure_race_distribution(clicked, value):
    last_clicked = clicked[-3:]
    if last_clicked == 'nan' or last_clicked == 'del':
        if last_clicked == 'del' or (last_clicked == 'del' and (value is None or value is '')):
            queryBarLogicObject.icd_list_race_cd.clear()
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'race_cd')
        return race_graph_builder.build_race_graph(df_patients)
    if last_clicked != 'nan' and (value is None or value is ''):
        raise PreventUpdate('No Changing!')
    if last_clicked == 'add':
        df_code = data_frame_logic.generate_df_icd_code(queryBarLogicObject, value)
        queryBarLogicObject.append_icd_list_race_cd(df_code.loc[0].values[0])
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'race_cd')
        return race_graph_builder.build_race_graph(df_patients)


@app.callback(
    Output('age-distribution', 'figure'),
    [Input('clicked-button', 'children')],
    [State('input-box', 'value')]
)
def update_figure_age_distribution(clicked, value):
    last_clicked = clicked[-3:]
    if last_clicked == 'nan' or last_clicked == 'del':
        if last_clicked == 'del' or (last_clicked == 'del' and (value is None or value is '')):
            queryBarLogicObject.icd_list_age_in_years_num.clear()
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'age_in_years_num')
        return age_graph_builder.build_age_graph(df_patients)
    if last_clicked != 'nan' and (value is None or value is ''):
        raise PreventUpdate('No Changing!')
    if last_clicked == 'add':
        df_code = data_frame_logic.generate_df_icd_code(queryBarLogicObject, value)
        queryBarLogicObject.append_icd_list_age_in_years_num(df_code.loc[0].values[0])
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'age_in_years_num')
        return age_graph_builder.build_age_graph(df_patients)


# @app.callback(
#     Output('language-distribution', 'figure'),
#     [Input('clicked-button', 'children')],
#     [State('input-box', 'value')]
# )
# def update_figure_language_distribution(clicked, value):
#     last_clicked = clicked[-3:]
#     if last_clicked == 'nan' or last_clicked == 'del':
#         if last_clicked == 'del' or (last_clicked == 'del' and (value is None or value is '')):
#             queryBarLogicObject.icd_list_language_cd.clear()
#         df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'language_cd')
#         return language_graph_builder.build_language_graph(df_patients)
#     if last_clicked != 'nan' and (value is None or value is ''):
#         raise PreventUpdate('No Changing!')
#     if last_clicked == 'add':
#         df_code = data_frame_logic.generate_df_icd_code(queryBarLogicObject, value)
#         queryBarLogicObject.append_icd_list_language_cd(df_code.loc[0].values[0])
#         df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'language_cd')
#         return language_graph_builder.build_language_graph(df_patients)


# Zuordnung der Buttons
@app.callback(
    Output('clicked-button', 'children'),
    [Input('del-button', 'n_clicks'),
     Input('add-button', 'n_clicks')],
    [State('clicked-button', 'children')]
)
def update_clicked(del_clicks, add_clicks, prev_clicks):
    prev_clicks = dict([i.split(':') for i in prev_clicks.split(' ')])
    last_clicked = 'nan'

    if del_clicks > int(prev_clicks['del']):
        last_clicked = 'del'
    elif add_clicks > int(prev_clicks['add']):
        last_clicked = 'add'

    cur_clicks = 'del:{} add:{} last:{}'.format(del_clicks, add_clicks, last_clicked)

    return cur_clicks


if __name__ == "__main__":
    app.run_server(debug=True, port=5001)
