# @app.callback([
#
#     Output('decimal', 'children'),
#     Output('sex-distribution', 'figure'),
#     Output('race-distribution', 'figure'),
#     Output('age-distribution', 'figure')],
#     [Input('clicked-button', 'children'),
#      Input('con1-button', 'n_clicks'),
#      Input('con2-button', 'n_clicks')],
#     [State('input-box', 'value')]
# )
# def update_results(clicked, con1_clicks, con2_clicks, value):
#     last_clicked = clicked[-3:]
#     if last_clicked == 'nan' or last_clicked == 'del':
#         if last_clicked == 'del' or (last_clicked == 'del' and (value is None or value is '')):
#             queryBarLogicObject.icd_list.clear()
#         df_patients_decimal = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'decimal')
#         count_patients = len(df_patients_decimal)
#         df_patients_sex = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'sex_cd')
#         df_patients_race = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'race_cd')
#         df_patients_age = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'age_in_years_num')
#         return html.H5('Anzahl Patienten: ' + str(count_patients)), sex_graph_builder.build_sex_graph(df_patients_sex), \
#                race_graph_builder.build_race_graph(df_patients_race), age_graph_builder.build_age_graph(df_patients_age)
#     if last_clicked != 'nan' and (value is None or value is ''):
#         raise PreventUpdate('No Changing!')
#     if last_clicked == 'co1':
#         if con1_clicks % 2 == 1:
#             queryBarLogicObject.name_list[1] = ' OR '
#         if con1_clicks % 2 == 0:
#             queryBarLogicObject.name_list[1] = ' AND '
#         df_patients_decimal = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'decimal')
#         count_patients = len(df_patients_decimal)
#         df_patients_sex = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'sex_cd')
#         df_patients_race = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'race_cd')
#         df_patients_age = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'age_in_years_num')
#         return html.H5('Anzahl Patienten: ' + str(count_patients)), sex_graph_builder.build_sex_graph(df_patients_sex), \
#                race_graph_builder.build_race_graph(df_patients_race), age_graph_builder.build_age_graph(df_patients_age)
#     if last_clicked == 'co2':
#         if con2_clicks % 2 == 1:
#             queryBarLogicObject.name_list[3] = ' OR '
#         if con2_clicks % 2 == 0:
#             queryBarLogicObject.name_list[3] = ' AND '
#         df_patients_decimal = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'decimal')
#         count_patients = len(df_patients_decimal)
#         df_patients_sex = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'sex_cd')
#         df_patients_race = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'race_cd')
#         df_patients_age = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'age_in_years_num')
#         return html.H5('Anzahl Patienten: ' + str(count_patients)), sex_graph_builder.build_sex_graph(df_patients_sex), \
#                race_graph_builder.build_race_graph(df_patients_race), age_graph_builder.build_age_graph(df_patients_age)
#     if last_clicked == 'add':
#         df_code = data_frame_logic.generate_df_icd_code(queryBarLogicObject, value)
#         queryBarLogicObject.append_icd_list(df_code.loc[0].values[0])
#         df_patients_decimal = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'decimal')
#         count_patients = len(df_patients_decimal)
#         df_patients_sex = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'sex_cd')
#         df_patients_race = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'race_cd')
#         df_patients_age = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'age_in_years_num')
#         return html.H5('Anzahl Patienten: ' + str(count_patients)), sex_graph_builder.build_sex_graph(df_patients_sex), \
#                race_graph_builder.build_race_graph(df_patients_race), age_graph_builder.build_age_graph(df_patients_age)
