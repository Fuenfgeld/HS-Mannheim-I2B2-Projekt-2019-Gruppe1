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

    navigationBarObject.layoutSearchBar,

    navigationBarObject.layout_navigation,

    queryBarObject.layout_delete_button,

    queryBarObject.layout_query_bar,

    resultsObject.layout_results

])

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})


@app.callback([
    Output('criteria1-div', 'hidden'),
    Output('criteria1-div', 'children'),
    Output('con1-button', 'style'),
    Output('con1-button', 'children'),
    Output('criteria2-div', 'hidden'),
    Output('criteria2-div', 'children')],
    [Input('clicked-button', 'children'),
     Input('con1-button', 'n_clicks')],
    [State('input-box', 'value')]
)
def update_criteria_divs(clicked, n_clicks, value):
    last_clicked = clicked[-3:]
    if last_clicked == 'nan':
        return True, '', {'display': 'none'}, html.H5(''), True, ''
    if last_clicked == 'del' or (last_clicked == 'del' and (value is None or value is '')):
        queryBarLogicObject.name_list.clear()
        return True, '', {'display': 'none'}, html.H5(''), True, ''
    if last_clicked == 'co1':
        if n_clicks % 2 == 1:
            return False, queryBarLogicObject.name_list[0], {'display': 'block'}, html.H5('OR'), False, \
                   queryBarLogicObject.name_list[2]
        if n_clicks % 2 == 0:
            return False, queryBarLogicObject.name_list[0], {'display': 'block'}, html.H5('AND'), False, \
                   queryBarLogicObject.name_list[2]
    if last_clicked != 'nan' and (value is None or value is ''):
        raise PreventUpdate('No Changing!')
    if last_clicked == 'add':
        if len(queryBarLogicObject.name_list) == 0:
            queryBarLogicObject.append_name_list(value)
            return False, value, {'display': 'none'}, html.H5(''), True, ''
        if len(queryBarLogicObject.name_list) == 1:
            queryBarLogicObject.append_name_list(value)
            return False, queryBarLogicObject.name_list[0], {'display': 'block'}, html.H5('AND'), False, value
        else:
            raise PreventUpdate('No Changing!')


@app.callback([

    Output('decimal', 'children'),
    Output('sex-distribution', 'figure'),
    Output('race-distribution', 'figure'),
    Output('age-distribution', 'figure')],
    [Input('clicked-button', 'children'),
     Input('con1-button', 'n_clicks')],
    [State('input-box', 'value')]
)
def update_results(clicked, n_clicks, value):
    last_clicked = clicked[-3:]
    if last_clicked == 'nan' or last_clicked == 'del':
        if last_clicked == 'del' or (last_clicked == 'del' and (value is None or value is '')):
            queryBarLogicObject.icd_list.clear()
        df_patients_decimal = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'decimal')
        count_patients = len(df_patients_decimal)
        df_patients_sex = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'sex_cd')
        df_patients_race = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'race_cd')
        df_patients_age = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'age_in_years_num')
        return html.H5('Anzahl Patienten: ' + str(count_patients)), sex_graph_builder.build_sex_graph(df_patients_sex), \
               race_graph_builder.build_race_graph(df_patients_race), age_graph_builder.build_age_graph(df_patients_age)
    if last_clicked != 'nan' and (value is None or value is ''):
        raise PreventUpdate('No Changing!')
    if last_clicked == 'co1':
        if n_clicks % 2 == 1:
            queryBarLogicObject.name_list[1] = ' OR '
        if n_clicks % 2 == 0:
            queryBarLogicObject.name_list[1] = ' AND '
        df_patients_decimal = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'decimal')
        count_patients = len(df_patients_decimal)
        df_patients_sex = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'sex_cd')
        df_patients_race = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'race_cd')
        df_patients_age = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'age_in_years_num')
        return html.H5('Anzahl Patienten: ' + str(count_patients)), sex_graph_builder.build_sex_graph(df_patients_sex), \
               race_graph_builder.build_race_graph(df_patients_race), age_graph_builder.build_age_graph(df_patients_age)
    if last_clicked == 'add':
        df_code = data_frame_logic.generate_df_icd_code(queryBarLogicObject, value)
        queryBarLogicObject.append_icd_list(df_code.loc[0].values[0])
        df_patients_decimal = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'decimal')
        count_patients = len(df_patients_decimal)
        df_patients_sex = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'sex_cd')
        df_patients_race = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'race_cd')
        df_patients_age = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'age_in_years_num')
        return html.H5('Anzahl Patienten: ' + str(count_patients)), sex_graph_builder.build_sex_graph(df_patients_sex), \
               race_graph_builder.build_race_graph(df_patients_race), age_graph_builder.build_age_graph(df_patients_age)


# Zuordnung der Buttons
@app.callback(
    Output('clicked-button', 'children'),
    [Input('del-button', 'n_clicks'),
     Input('add-button', 'n_clicks'),
     Input('con1-button', 'n_clicks')],
    [State('clicked-button', 'children')]
)
def update_clicked(del_clicks, add_clicks, con1_clicks, prev_clicks):
    prev_clicks = dict([i.split(':') for i in prev_clicks.split(' ')])
    last_clicked = 'nan'

    if del_clicks > int(prev_clicks['del']):
        last_clicked = 'del'
    elif add_clicks > int(prev_clicks['add']):
        last_clicked = 'add'
    elif con1_clicks > int(prev_clicks['co1']):
        last_clicked = 'co1'

    cur_clicks = 'del:{} add:{} co1:{} last:{}'.format(del_clicks, add_clicks, con1_clicks, last_clicked)

    return cur_clicks


if __name__ == "__main__":
    app.run_server(debug=True, port=5001)
