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
from backend.graph_logic import decimal_logic
from backend.graph_logic import income_graph_builder
from backend.graph_logic import language_graph_builder
from backend.graph_logic import besides_diagnoses_graph_builder

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

    navigationBarObject.layout_search_bar,

    navigationBarObject.layout_navigation,

    queryBarObject.layout_delete_button,

    queryBarObject.layout_query_bar,

    resultsObject.layout_checkout,
    resultsObject.layout_decimal,

    resultsObject.layout_results

])

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

@app.callback(
    Output('sex-distribution', 'style'),
    [Input('checklistSEX', 'values')])
def update_radiobutton(visibility_state):
    if visibility_state == ['on']:
        return {'display': 'block'}
    else:
        return {'display': 'none'}

@app.callback(
    Output('race-distribution', 'style'),
    [Input('checklistRace', 'values')])
def update_radiobutton(visibility_state):
    if visibility_state == ['on']:
        return {'display': 'block'}
    else:
        return {'display': 'none'}

@app.callback(
    Output('age-distribution', 'style'),
    [Input('checklistAGE', 'values')])
def update_radiobutton(visibility_state):
    if visibility_state == ['on']:
        return {'display': 'block'}
    else:
        return {'display': 'none'}

@app.callback(
    Output('income-distribution', 'style'),
    [Input('checklistIncome', 'values')])
def update_radiobutton(visibility_state):
    if visibility_state == ['off']:
        return {'display': 'none'}
    else:
        return {'display': 'block'}

@app.callback(
    Output('language-distribution', 'style'),
    [Input('checklistLanguage', 'values')])
def update_radiobutton(visibility_state):
    if visibility_state == ['off']:
        return {'display': 'none'}
    else:
        return {'display': 'block'}

@app.callback(
    Output('besides-diagnoses', 'style'),
    [Input('checklistBesides', 'values')])
def update_radiobutton(visibility_state):
    if visibility_state == ['on']:
        return {'display': 'block'}
    else:
        return {'display': 'none'}

con_list = []
con_list.append('AND')
con_list.append('AND')


@app.callback([
    Output('criteria1-div', 'hidden'),
    Output('criteria1-div', 'children'),
    Output('con1-button', 'style'),
    Output('con1-button', 'children'),
    Output('criteria2-div', 'hidden'),
    Output('criteria2-div', 'children'),
    Output('con2-button', 'style'),
    Output('con2-button', 'children'),
    Output('criteria3-div', 'hidden'),
    Output('criteria3-div', 'children'),
    Output('decimal', 'children'),
    Output('sex-distribution', 'figure'),
    Output('race-distribution', 'figure'),
    Output('age-distribution', 'figure'),
    Output('income-distribution', 'figure'),
    Output('language-distribution', 'figure'),
    Output('besides-diagnoses', 'figure')],
    [Input('clicked-button', 'children')],
    [State('input-box', 'value'),
     State('criteria3-div', 'hidden')]
)
def update_all(clicked, value, hidden):
    last_clicked = clicked[-3:]
    if last_clicked == 'nan' or last_clicked == 'del':
        if last_clicked == 'del' or (last_clicked == 'del' and (value is None or value is '')):
            queryBarLogicObject.name_list.clear()
            queryBarLogicObject.icd_list.clear()
            con_list[0] = 'AND'
            con_list[1] = 'AND'
        return True, '', {'display': 'none'}, html.H5(''), True, '', {'display': 'none'}, html.H5(''), \
               True, '', decimal_logic.build_decimal(queryBarLogicObject), \
               sex_graph_builder.build_sex_graph(queryBarLogicObject), \
               race_graph_builder.build_race_graph(queryBarLogicObject), \
               age_graph_builder.build_age_graph(queryBarLogicObject), \
               income_graph_builder.build_income_graph(queryBarLogicObject), \
               language_graph_builder.build_language_graph(queryBarLogicObject), \
               besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicObject)
    if last_clicked != 'nan' and (value is None or value is ''):
        raise PreventUpdate('No Changing!')
    if last_clicked == 'co1':
        if (con_list[0] == 'AND') & hidden:
            con_list[0] = 'OR'
            queryBarLogicObject.name_list[1] = ' OR '
            return False, queryBarLogicObject.name_list[0], {'display': 'block'}, html.H5('OR'), False, \
                   queryBarLogicObject.name_list[2], {'display': 'none'}, html.H5(''), \
                   True, '', decimal_logic.build_decimal(queryBarLogicObject), \
                   sex_graph_builder.build_sex_graph(queryBarLogicObject), \
                   race_graph_builder.build_race_graph(queryBarLogicObject), \
                   age_graph_builder.build_age_graph(queryBarLogicObject), \
                   income_graph_builder.build_income_graph(queryBarLogicObject), \
                   language_graph_builder.build_language_graph(queryBarLogicObject), \
                   besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicObject)
        if (con_list[0] == 'OR') & hidden:
            con_list[0] = 'AND'
            queryBarLogicObject.name_list[1] = ' AND '
            return False, queryBarLogicObject.name_list[0], {'display': 'block'}, html.H5('AND'), False, \
                   queryBarLogicObject.name_list[2], {'display': 'none'}, html.H5(''), \
                   True, '', decimal_logic.build_decimal(queryBarLogicObject), \
                   sex_graph_builder.build_sex_graph(queryBarLogicObject), \
                   race_graph_builder.build_race_graph(queryBarLogicObject), \
                   age_graph_builder.build_age_graph(queryBarLogicObject), \
                   income_graph_builder.build_income_graph(queryBarLogicObject), \
                   language_graph_builder.build_language_graph(queryBarLogicObject), \
                   besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicObject)
        if (con_list[0] == 'AND') & (not hidden):
            if con_list[1] == 'AND':
                con_list[0] = 'OR'
                queryBarLogicObject.name_list[1] = ' OR '
                return False, queryBarLogicObject.name_list[0], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicObject.name_list[2], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicObject.name_list[4], decimal_logic.build_decimal(queryBarLogicObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicObject), \
                       race_graph_builder.build_race_graph(queryBarLogicObject), \
                       age_graph_builder.build_age_graph(queryBarLogicObject), \
                       income_graph_builder.build_income_graph(queryBarLogicObject), \
                       language_graph_builder.build_language_graph(queryBarLogicObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicObject)
            if con_list[1] == 'OR':
                con_list[0] = 'OR'
                queryBarLogicObject.name_list[1] = ' OR '
                return False, queryBarLogicObject.name_list[0], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicObject.name_list[2], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicObject.name_list[4], decimal_logic.build_decimal(queryBarLogicObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicObject), \
                       race_graph_builder.build_race_graph(queryBarLogicObject), \
                       age_graph_builder.build_age_graph(queryBarLogicObject), \
                       income_graph_builder.build_income_graph(queryBarLogicObject), \
                       language_graph_builder.build_language_graph(queryBarLogicObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicObject)
        if (con_list[0] == 'OR') & (not hidden):
            if con_list[1] == 'AND':
                con_list[0] = 'AND'
                queryBarLogicObject.name_list[1] = ' AND '
                return False, queryBarLogicObject.name_list[0], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicObject.name_list[2], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicObject.name_list[4], decimal_logic.build_decimal(queryBarLogicObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicObject), \
                       race_graph_builder.build_race_graph(queryBarLogicObject), \
                       age_graph_builder.build_age_graph(queryBarLogicObject), \
                       income_graph_builder.build_income_graph(queryBarLogicObject), \
                       language_graph_builder.build_language_graph(queryBarLogicObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicObject)
            if con_list[1] == 'OR':
                con_list[0] = 'AND'
                queryBarLogicObject.name_list[1] = ' AND '
                return False, queryBarLogicObject.name_list[0], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicObject.name_list[2], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicObject.name_list[4], decimal_logic.build_decimal(queryBarLogicObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicObject), \
                       race_graph_builder.build_race_graph(queryBarLogicObject), \
                       age_graph_builder.build_age_graph(queryBarLogicObject), \
                       income_graph_builder.build_income_graph(queryBarLogicObject), \
                       language_graph_builder.build_language_graph(queryBarLogicObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicObject)
    if last_clicked == 'co2':
        if con_list[0] == 'AND':
            if con_list[1] == 'AND':
                con_list[1] = 'OR'
                queryBarLogicObject.name_list[3] = ' OR '
                return False, queryBarLogicObject.name_list[0], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicObject.name_list[2], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicObject.name_list[4], decimal_logic.build_decimal(queryBarLogicObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicObject), \
                       race_graph_builder.build_race_graph(queryBarLogicObject), \
                       age_graph_builder.build_age_graph(queryBarLogicObject), \
                       income_graph_builder.build_income_graph(queryBarLogicObject), \
                       language_graph_builder.build_language_graph(queryBarLogicObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicObject)
            if con_list[1] == 'OR':
                con_list[1] = 'AND'
                queryBarLogicObject.name_list[3] = ' AND '
                return False, queryBarLogicObject.name_list[0], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicObject.name_list[2], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicObject.name_list[4], decimal_logic.build_decimal(queryBarLogicObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicObject), \
                       race_graph_builder.build_race_graph(queryBarLogicObject), \
                       age_graph_builder.build_age_graph(queryBarLogicObject), \
                       income_graph_builder.build_income_graph(queryBarLogicObject), \
                       language_graph_builder.build_language_graph(queryBarLogicObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicObject)
        if con_list[0] == 'OR':
            if con_list[1] == 'AND':
                con_list[1] = 'OR'
                queryBarLogicObject.name_list[3] = ' OR '
                return False, queryBarLogicObject.name_list[0], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicObject.name_list[2], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicObject.name_list[4], decimal_logic.build_decimal(queryBarLogicObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicObject), \
                       race_graph_builder.build_race_graph(queryBarLogicObject), \
                       age_graph_builder.build_age_graph(queryBarLogicObject), \
                       income_graph_builder.build_income_graph(queryBarLogicObject), \
                       language_graph_builder.build_language_graph(queryBarLogicObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicObject)
            if con_list[1] == 'OR':
                con_list[1] = 'AND'
                queryBarLogicObject.name_list[3] = ' AND '
                return False, queryBarLogicObject.name_list[0], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicObject.name_list[2], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicObject.name_list[4], decimal_logic.build_decimal(queryBarLogicObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicObject), \
                       race_graph_builder.build_race_graph(queryBarLogicObject), \
                       age_graph_builder.build_age_graph(queryBarLogicObject), \
                       income_graph_builder.build_income_graph(queryBarLogicObject), \
                       language_graph_builder.build_language_graph(queryBarLogicObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicObject)
    if last_clicked == 'add':
        if len(queryBarLogicObject.name_list) == 0:
            queryBarLogicObject.append_name_list(value)
            queryBarLogicObject.append_icd_list(queryBarLogicObject, value)
            return False, value, {'display': 'none'}, html.H5(''), True, '', {'display': 'none'}, html.H5(''), \
                   True, '', decimal_logic.build_decimal(queryBarLogicObject), \
                   sex_graph_builder.build_sex_graph(queryBarLogicObject), \
                   race_graph_builder.build_race_graph(queryBarLogicObject), \
                   age_graph_builder.build_age_graph(queryBarLogicObject), \
                   income_graph_builder.build_income_graph(queryBarLogicObject), \
                   language_graph_builder.build_language_graph(queryBarLogicObject), \
                   besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicObject)

        if len(queryBarLogicObject.name_list) == 1:
            queryBarLogicObject.append_name_list(value)
            queryBarLogicObject.append_icd_list(queryBarLogicObject, value)
            return False, queryBarLogicObject.name_list[0], {'display': 'block'}, html.H5('AND'), False, value, {
                'display': 'none'}, html.H5(''), True, '', decimal_logic.build_decimal(queryBarLogicObject), \
                   sex_graph_builder.build_sex_graph(queryBarLogicObject), \
                   race_graph_builder.build_race_graph(queryBarLogicObject), \
                   age_graph_builder.build_age_graph(queryBarLogicObject), \
                   income_graph_builder.build_income_graph(queryBarLogicObject), \
                   language_graph_builder.build_language_graph(queryBarLogicObject), \
                   besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicObject)
        if len(queryBarLogicObject.name_list) == 3:
            queryBarLogicObject.append_name_list(value)
            queryBarLogicObject.append_icd_list(queryBarLogicObject, value)
            if con_list[0] == 'AND':
                return False, queryBarLogicObject.name_list[0], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicObject.name_list[2], {'display': 'block'}, html.H5('AND'), False, value, \
                       decimal_logic.build_decimal(queryBarLogicObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicObject), \
                       race_graph_builder.build_race_graph(queryBarLogicObject), \
                       age_graph_builder.build_age_graph(queryBarLogicObject), \
                       income_graph_builder.build_income_graph(queryBarLogicObject), \
                       language_graph_builder.build_language_graph(queryBarLogicObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicObject)
            if con_list[0] == 'OR':
                return False, queryBarLogicObject.name_list[0], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicObject.name_list[2], {'display': 'block'}, html.H5('AND'), False, value, \
                       decimal_logic.build_decimal(queryBarLogicObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicObject), \
                       race_graph_builder.build_race_graph(queryBarLogicObject), \
                       age_graph_builder.build_age_graph(queryBarLogicObject), \
                       income_graph_builder.build_income_graph(queryBarLogicObject), \
                       language_graph_builder.build_language_graph(queryBarLogicObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicObject)
        else:
            raise PreventUpdate('No Changing!')


# Zuordnung der Buttons
@app.callback(
    Output('clicked-button', 'children'),
    [Input('del-button', 'n_clicks'),
     Input('add-button', 'n_clicks'),
     Input('con1-button', 'n_clicks'),
     Input('con2-button', 'n_clicks')],
    [State('clicked-button', 'children')]
)
def update_clicked(del_clicks, add_clicks, con1_clicks, con2_clicks, prev_clicks):
    prev_clicks = dict([i.split(':') for i in prev_clicks.split(' ')])
    last_clicked = 'nan'

    if del_clicks > int(prev_clicks['del']):
        last_clicked = 'del'
    elif add_clicks > int(prev_clicks['add']):
        last_clicked = 'add'
    elif con1_clicks > int(prev_clicks['co1']):
        last_clicked = 'co1'
    elif con2_clicks > int(prev_clicks['co2']):
        last_clicked = 'co2'

    cur_clicks = 'del:{} add:{} co1:{} co2:{} last:{}'.format(del_clicks, add_clicks, con1_clicks, con2_clicks,
                                                              last_clicked)

    return cur_clicks


if __name__ == "__main__":
    app.run_server(debug=True, port=5001)

