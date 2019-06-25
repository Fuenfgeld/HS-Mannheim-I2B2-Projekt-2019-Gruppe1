import dash
import dash_html_components as html
from dash.exceptions import PreventUpdate
from dash.dependencies import Output, Input, State

from frontend.app_layout import layout_banner
from frontend.app_layout import layout_query_bar
from frontend.app_layout import layout_navigation_bar
from frontend.app_layout import layout_results

from backend.graph_logic import age_graph_builder
from backend.graph_logic import sex_graph_builder
from backend.graph_logic import race_graph_builder
from backend.graph_logic import decimal_logic
from backend.graph_logic import income_graph_builder
from backend.graph_logic import language_graph_builder
from backend.graph_logic import besides_diagnoses_graph_builder
from backend.query_bar_logic import query_bar_logic_new
from backend.result_logic import result_merge

bannerObject = layout_banner.layoutBanner()
queryBarObject = layout_query_bar.layoutQueryBar()
navigationBarObject = layout_navigation_bar.layoutNavigationBar()
resultsObject = layout_results.layoutResults()
queryBarLogicNewObject = query_bar_logic_new.queryBarLogicNew()
resultMergeObject = result_merge.resultMerge()

app = dash.Dash(__name__)

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


# callback for event

@app.callback(
    Output('input-box', 'value'),
    [Input('javascript', 'event')])
def myfunc(event):
    if event is not None:
        string = str(event)[7:-12]
        return string


@app.callback(
    Output('input-box', 'className'),
    [Input('clicked-button', 'children')]
)
def clear_class(clicked):
    last_clicked = clicked[-3:]
    if last_clicked == 'add':
        return ''


# callback for visualization

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
    Output('besides-diagnoses', 'figure')
],
    [Input('clicked-button', 'children')],
    [State('input-box', 'value'),
     State('criteria3-div', 'hidden')]
)
def update_all(clicked, value, hidden):
    last_clicked = clicked[-3:]

    if last_clicked == 'nan' or last_clicked == 'del':
        if last_clicked == 'del' or (last_clicked == 'del' and (value is None or value is '')):
            queryBarLogicNewObject.delete_all()
        return True, '', {'display': 'none'}, html.H5(''), True, '', {'display': 'none'}, html.H5(''), \
               True, '', decimal_logic.build_decimal(queryBarLogicNewObject, resultMergeObject), \
               sex_graph_builder.build_sex_graph(queryBarLogicNewObject, resultMergeObject), \
               race_graph_builder.build_race_graph(queryBarLogicNewObject, resultMergeObject), \
               age_graph_builder.build_age_graph(queryBarLogicNewObject, resultMergeObject), \
               income_graph_builder.build_income_graph(queryBarLogicNewObject, resultMergeObject), \
               language_graph_builder.build_language_graph(queryBarLogicNewObject, resultMergeObject), \
               besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicNewObject, resultMergeObject)
    if last_clicked != 'nan' and (value is None or value is ''):
        raise PreventUpdate('No Changing!')
    if last_clicked == 'co1':
        if (queryBarLogicNewObject.con_list[0] == 'AND') & hidden:
            queryBarLogicNewObject.con_list[0] = 'OR'
            queryBarLogicNewObject.update_current_over_all_df()
            return False, queryBarLogicNewObject.name_list[0], {'display': 'block'}, html.H5('OR'), False, \
                   queryBarLogicNewObject.name_list[1], {'display': 'none'}, html.H5(''), \
                   True, '', decimal_logic.build_decimal(queryBarLogicNewObject, resultMergeObject), \
                   sex_graph_builder.build_sex_graph(queryBarLogicNewObject, resultMergeObject), \
                   race_graph_builder.build_race_graph(queryBarLogicNewObject, resultMergeObject), \
                   age_graph_builder.build_age_graph(queryBarLogicNewObject, resultMergeObject), \
                   income_graph_builder.build_income_graph(queryBarLogicNewObject, resultMergeObject), \
                   language_graph_builder.build_language_graph(queryBarLogicNewObject, resultMergeObject), \
                   besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicNewObject,
                                                                                 resultMergeObject)
        if (queryBarLogicNewObject.con_list[0] == 'OR') & hidden:
            queryBarLogicNewObject.con_list[0] = 'AND'
            queryBarLogicNewObject.update_current_over_all_df()
            return False, queryBarLogicNewObject.name_list[0], {'display': 'block'}, html.H5('AND'), False, \
                   queryBarLogicNewObject.name_list[1], {'display': 'none'}, html.H5(''), \
                   True, '', decimal_logic.build_decimal(queryBarLogicNewObject, resultMergeObject), \
                   sex_graph_builder.build_sex_graph(queryBarLogicNewObject, resultMergeObject), \
                   race_graph_builder.build_race_graph(queryBarLogicNewObject, resultMergeObject), \
                   age_graph_builder.build_age_graph(queryBarLogicNewObject, resultMergeObject), \
                   income_graph_builder.build_income_graph(queryBarLogicNewObject, resultMergeObject), \
                   language_graph_builder.build_language_graph(queryBarLogicNewObject, resultMergeObject), \
                   besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicNewObject,
                                                                                 resultMergeObject)
        if (queryBarLogicNewObject.con_list[0] == 'AND') & (not hidden):
            if queryBarLogicNewObject.con_list[1] == 'AND':
                queryBarLogicNewObject.con_list[0] = 'OR'
                queryBarLogicNewObject.update_current_over_all_df()
                return False, queryBarLogicNewObject.name_list[0], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicNewObject.name_list[1], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicNewObject.name_list[2], decimal_logic.build_decimal(queryBarLogicNewObject,
                                                                                        resultMergeObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicNewObject, resultMergeObject), \
                       race_graph_builder.build_race_graph(queryBarLogicNewObject, resultMergeObject), \
                       age_graph_builder.build_age_graph(queryBarLogicNewObject, resultMergeObject), \
                       income_graph_builder.build_income_graph(queryBarLogicNewObject, resultMergeObject), \
                       language_graph_builder.build_language_graph(queryBarLogicNewObject, resultMergeObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicNewObject,
                                                                                     resultMergeObject)
            if queryBarLogicNewObject.con_list[1] == 'OR':
                queryBarLogicNewObject.con_list[0] = 'OR'
                queryBarLogicNewObject.update_current_over_all_df()
                return False, queryBarLogicNewObject.name_list[0], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicNewObject.name_list[1], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicNewObject.name_list[2], decimal_logic.build_decimal(queryBarLogicNewObject,
                                                                                        resultMergeObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicNewObject, resultMergeObject), \
                       race_graph_builder.build_race_graph(queryBarLogicNewObject, resultMergeObject), \
                       age_graph_builder.build_age_graph(queryBarLogicNewObject, resultMergeObject), \
                       income_graph_builder.build_income_graph(queryBarLogicNewObject, resultMergeObject), \
                       language_graph_builder.build_language_graph(queryBarLogicNewObject, resultMergeObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicNewObject,
                                                                                     resultMergeObject)
        if (queryBarLogicNewObject.con_list[0] == 'OR') & (not hidden):
            if queryBarLogicNewObject.con_list[1] == 'AND':
                queryBarLogicNewObject.con_list[0] = 'AND'
                queryBarLogicNewObject.update_current_over_all_df()
                return False, queryBarLogicNewObject.name_list[0], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicNewObject.name_list[1], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicNewObject.name_list[2], decimal_logic.build_decimal(queryBarLogicNewObject,
                                                                                        resultMergeObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicNewObject, resultMergeObject), \
                       race_graph_builder.build_race_graph(queryBarLogicNewObject, resultMergeObject), \
                       age_graph_builder.build_age_graph(queryBarLogicNewObject, resultMergeObject), \
                       income_graph_builder.build_income_graph(queryBarLogicNewObject, resultMergeObject), \
                       language_graph_builder.build_language_graph(queryBarLogicNewObject, resultMergeObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicNewObject,
                                                                                     resultMergeObject)
            if queryBarLogicNewObject.con_list[1] == 'OR':
                queryBarLogicNewObject.con_list[0] = 'AND'
                queryBarLogicNewObject.update_current_over_all_df()
                return False, queryBarLogicNewObject.name_list[0], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicNewObject.name_list[1], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicNewObject.name_list[2], decimal_logic.build_decimal(queryBarLogicNewObject,
                                                                                        resultMergeObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicNewObject, resultMergeObject), \
                       race_graph_builder.build_race_graph(queryBarLogicNewObject, resultMergeObject), \
                       age_graph_builder.build_age_graph(queryBarLogicNewObject, resultMergeObject), \
                       income_graph_builder.build_income_graph(queryBarLogicNewObject, resultMergeObject), \
                       language_graph_builder.build_language_graph(queryBarLogicNewObject, resultMergeObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicNewObject,
                                                                                     resultMergeObject)
    if last_clicked == 'co2':
        if queryBarLogicNewObject.con_list[0] == 'AND':
            if queryBarLogicNewObject.con_list[1] == 'AND':
                queryBarLogicNewObject.con_list[1] = 'OR'
                queryBarLogicNewObject.update_current_over_all_df()
                return False, queryBarLogicNewObject.name_list[0], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicNewObject.name_list[1], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicNewObject.name_list[2], decimal_logic.build_decimal(queryBarLogicNewObject,
                                                                                        resultMergeObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicNewObject, resultMergeObject), \
                       race_graph_builder.build_race_graph(queryBarLogicNewObject, resultMergeObject), \
                       age_graph_builder.build_age_graph(queryBarLogicNewObject, resultMergeObject), \
                       income_graph_builder.build_income_graph(queryBarLogicNewObject, resultMergeObject), \
                       language_graph_builder.build_language_graph(queryBarLogicNewObject, resultMergeObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicNewObject,
                                                                                     resultMergeObject)
            if queryBarLogicNewObject.con_list[1] == 'OR':
                queryBarLogicNewObject.con_list[1] = 'AND'
                queryBarLogicNewObject.update_current_over_all_df()
                return False, queryBarLogicNewObject.name_list[0], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicNewObject.name_list[1], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicNewObject.name_list[2], decimal_logic.build_decimal(queryBarLogicNewObject,
                                                                                        resultMergeObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicNewObject, resultMergeObject), \
                       race_graph_builder.build_race_graph(queryBarLogicNewObject, resultMergeObject), \
                       age_graph_builder.build_age_graph(queryBarLogicNewObject, resultMergeObject), \
                       income_graph_builder.build_income_graph(queryBarLogicNewObject, resultMergeObject), \
                       language_graph_builder.build_language_graph(queryBarLogicNewObject, resultMergeObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicNewObject,
                                                                                     resultMergeObject)
        if queryBarLogicNewObject.con_list[0] == 'OR':
            if queryBarLogicNewObject.con_list[1] == 'AND':
                queryBarLogicNewObject.con_list[1] = 'OR'
                queryBarLogicNewObject.update_current_over_all_df()
                return False, queryBarLogicNewObject.name_list[0], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicNewObject.name_list[1], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicNewObject.name_list[2], decimal_logic.build_decimal(queryBarLogicNewObject,
                                                                                        resultMergeObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicNewObject, resultMergeObject), \
                       race_graph_builder.build_race_graph(queryBarLogicNewObject, resultMergeObject), \
                       age_graph_builder.build_age_graph(queryBarLogicNewObject, resultMergeObject), \
                       income_graph_builder.build_income_graph(queryBarLogicNewObject, resultMergeObject), \
                       language_graph_builder.build_language_graph(queryBarLogicNewObject, resultMergeObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicNewObject,
                                                                                     resultMergeObject)
            if queryBarLogicNewObject.con_list[1] == 'OR':
                queryBarLogicNewObject.con_list[1] = 'AND'
                queryBarLogicNewObject.update_current_over_all_df()
                return False, queryBarLogicNewObject.name_list[0], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicNewObject.name_list[1], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicNewObject.name_list[2], decimal_logic.build_decimal(queryBarLogicNewObject,
                                                                                        resultMergeObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicNewObject, resultMergeObject), \
                       race_graph_builder.build_race_graph(queryBarLogicNewObject, resultMergeObject), \
                       age_graph_builder.build_age_graph(queryBarLogicNewObject, resultMergeObject), \
                       income_graph_builder.build_income_graph(queryBarLogicNewObject, resultMergeObject), \
                       language_graph_builder.build_language_graph(queryBarLogicNewObject, resultMergeObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicNewObject,
                                                                                     resultMergeObject)
    if last_clicked == 'add':
        if len(queryBarLogicNewObject.name_list) == 0:
            queryBarLogicNewObject.append_selection(value)
            return False, value, {'display': 'none'}, html.H5(''), True, '', {'display': 'none'}, html.H5(''), \
                   True, '', decimal_logic.build_decimal(queryBarLogicNewObject, resultMergeObject), \
                   sex_graph_builder.build_sex_graph(queryBarLogicNewObject, resultMergeObject), \
                   race_graph_builder.build_race_graph(queryBarLogicNewObject, resultMergeObject), \
                   age_graph_builder.build_age_graph(queryBarLogicNewObject, resultMergeObject), \
                   income_graph_builder.build_income_graph(queryBarLogicNewObject, resultMergeObject), \
                   language_graph_builder.build_language_graph(queryBarLogicNewObject, resultMergeObject), \
                   besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicNewObject,
                                                                                 resultMergeObject)

        if len(queryBarLogicNewObject.name_list) == 1:
            queryBarLogicNewObject.append_selection(value)
            return False, queryBarLogicNewObject.name_list[0], {'display': 'block'}, html.H5('AND'), False, value, {
                'display': 'none'}, html.H5(''), True, '', decimal_logic.build_decimal(queryBarLogicNewObject,
                                                                                       resultMergeObject), \
                   sex_graph_builder.build_sex_graph(queryBarLogicNewObject, resultMergeObject), \
                   race_graph_builder.build_race_graph(queryBarLogicNewObject, resultMergeObject), \
                   age_graph_builder.build_age_graph(queryBarLogicNewObject, resultMergeObject), \
                   income_graph_builder.build_income_graph(queryBarLogicNewObject, resultMergeObject), \
                   language_graph_builder.build_language_graph(queryBarLogicNewObject, resultMergeObject), \
                   besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicNewObject,
                                                                                 resultMergeObject)
        if len(queryBarLogicNewObject.name_list) == 2:
            queryBarLogicNewObject.append_selection(value)
            if queryBarLogicNewObject.con_list[0] == 'AND':
                return False, queryBarLogicNewObject.name_list[0], {'display': 'block'}, html.H5('AND'), False, \
                       queryBarLogicNewObject.name_list[1], {'display': 'block'}, html.H5('AND'), False, value, \
                       decimal_logic.build_decimal(queryBarLogicNewObject, resultMergeObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicNewObject, resultMergeObject), \
                       race_graph_builder.build_race_graph(queryBarLogicNewObject, resultMergeObject), \
                       age_graph_builder.build_age_graph(queryBarLogicNewObject, resultMergeObject), \
                       income_graph_builder.build_income_graph(queryBarLogicNewObject, resultMergeObject), \
                       language_graph_builder.build_language_graph(queryBarLogicNewObject, resultMergeObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicNewObject,
                                                                                     resultMergeObject)
            if queryBarLogicNewObject.con_list[0] == 'OR':
                return False, queryBarLogicNewObject.name_list[0], {'display': 'block'}, html.H5('OR'), False, \
                       queryBarLogicNewObject.name_list[1], {'display': 'block'}, html.H5('AND'), False, value, \
                       decimal_logic.build_decimal(queryBarLogicNewObject, resultMergeObject), \
                       sex_graph_builder.build_sex_graph(queryBarLogicNewObject, resultMergeObject), \
                       race_graph_builder.build_race_graph(queryBarLogicNewObject, resultMergeObject), \
                       age_graph_builder.build_age_graph(queryBarLogicNewObject, resultMergeObject), \
                       income_graph_builder.build_income_graph(queryBarLogicNewObject, resultMergeObject), \
                       language_graph_builder.build_language_graph(queryBarLogicNewObject, resultMergeObject), \
                       besides_diagnoses_graph_builder.build_besides_diagnoses_graph(queryBarLogicNewObject,
                                                                                     resultMergeObject)
        else:
            raise PreventUpdate('No Changing!')


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
    if visibility_state == ['off']:
        return {'display': 'none'}
    else:
        return {'display': 'block'}


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


# callback for assignment of the buttons

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
