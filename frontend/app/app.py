import dash
import dash_html_components as html
from dash.exceptions import PreventUpdate
from dash.dependencies import Output, Input, State
import plotly.graph_objs as go

# imports der Klassen zur Anzeige der Seite
from frontend.app_layout import layout_banner
from frontend.app_layout import layout_query_bar
from frontend.app_layout import layout_navigation_bar
from frontend.app_layout import layout_results

# imports für Logik und Datenbankanbindung
from backend.query_bar_logic import query_bar_logic
from backend.data_frame_logic import data_frame_logic

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

    queryBarObject.layout_button,

    queryBarObject.layout_query_bar,

    resultsObject.layout_results

])

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})


@app.callback(
    Output('query-bar', 'children'),
    [Input('clicked-button', 'children')],
    [State('input-box', 'value')]
)
def button_action(clicked, value):
    last_clicked = clicked[-3:]
    if last_clicked == 'nan':
        return 'Abfrageleiste'
    if last_clicked == 'del' or (last_clicked == 'del' and (value is None or value is '')):
        queryBarLogicObject.name_list.clear()
        return 'Abfrageleiste'
    if last_clicked != 'nan' and (value is None or value is ''):
        return 'Bitte Wert eingeben!'
    if last_clicked == 'add':
        queryBarLogicObject.append_name_list(value)
        result = '{}'.format(
            queryBarLogicObject.print_name_list())
        return result


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
    if last_clicked != 'nan' and (value is None or value is ''):
        raise PreventUpdate('No Changing!')
    if last_clicked == 'add':
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
    [Input('clicked-button', 'children')],
    [State('input-box', 'value')]
)
def update_figure_age_distribution(clicked, value):
    last_clicked = clicked[-3:]
    if last_clicked == 'nan' or last_clicked == 'del':
        if last_clicked == 'del' or (last_clicked == 'del' and (value is None or value is '')):
            queryBarLogicObject.icd_list_age_in_years_num.clear()
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'age_in_years_num')
        age_until_9 = (((df_patients['age_in_years_num']).ge(0)) & ((df_patients['age_in_years_num']).le(9))).sum()
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
                y=[age_until_9, age_until_17, age_until_34, age_until_44, age_until_54, age_until_64, age_until_74,
                   age_until_84,
                   age_greater_85],
                marker=dict(
                    color=['#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff',
                           '#4da6ff'],
                    line=dict(color='#a3a3c2', width=2)),
            ),
            ],

            'layout': go.Layout(
                title='Altersverteilung',
            )
        }
    if last_clicked != 'nan' and (value is None or value is ''):
        raise PreventUpdate('No Changing!')
    if last_clicked == 'add':
        df_code = data_frame_logic.generate_df_icd_code(queryBarLogicObject, value)
        queryBarLogicObject.append_icd_list_age_in_years_num(df_code.loc[0].values[0])
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'age_in_years_num')
        age_until_9 = (((df_patients['age_in_years_num']).ge(0)) & ((df_patients['age_in_years_num']).le(9))).sum()
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
                y=[age_until_9, age_until_17, age_until_34, age_until_44, age_until_54, age_until_64, age_until_74,
                   age_until_84,
                   age_greater_85],
                marker=dict(
                    color=['#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff', '#4da6ff',
                           '#4da6ff'],
                    line=dict(color='#a3a3c2', width=2)),
            ),
            ],

            'layout': go.Layout(
                title='Altersverteilung',
            )
        }


@app.callback(
    Output('language-distribution', 'figure'),
    [Input('clicked-button', 'children')],
    [State('input-box', 'value')]
)
def update_figure_language_distribution(clicked, value):
    last_clicked = clicked[-3:]
    if last_clicked == 'nan' or last_clicked == 'del':
        if last_clicked == 'del' or (last_clicked == 'del' and (value is None or value is '')):
            queryBarLogicObject.icd_list_language_cd.clear()
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
    if last_clicked != 'nan' and (value is None or value is ''):
        raise PreventUpdate('No Changing!')
    if last_clicked == 'add':
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
