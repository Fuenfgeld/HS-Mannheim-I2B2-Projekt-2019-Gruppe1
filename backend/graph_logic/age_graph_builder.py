import plotly.graph_objs as go
from backend.data_frame_logic import data_frame_logic


def build_age_graph(queryBarLogicObject):
    df_over_all = data_frame_logic.generate_df_age_in_years_num_patient_dimension()
    age_until_9_over_all = (((df_over_all['age_in_years_num']).ge(0)) & ((df_over_all['age_in_years_num']).le(9))).sum()
    age_until_17_over_all = (
            ((df_over_all['age_in_years_num']).ge(10)) & ((df_over_all['age_in_years_num']).le(17))).sum()
    age_until_34_over_all = (
            ((df_over_all['age_in_years_num']).ge(18)) & ((df_over_all['age_in_years_num']).le(34))).sum()
    age_until_44_over_all = (
            ((df_over_all['age_in_years_num']).ge(35)) & ((df_over_all['age_in_years_num']).le(44))).sum()
    age_until_54_over_all = (
            ((df_over_all['age_in_years_num']).ge(45)) & ((df_over_all['age_in_years_num']).le(54))).sum()
    age_until_64_over_all = (
            ((df_over_all['age_in_years_num']).ge(55)) & ((df_over_all['age_in_years_num']).le(64))).sum()
    age_until_74_over_all = (
            ((df_over_all['age_in_years_num']).ge(65)) & ((df_over_all['age_in_years_num']).le(74))).sum()
    age_until_84_over_all = (
            ((df_over_all['age_in_years_num']).ge(75)) & ((df_over_all['age_in_years_num']).le(84))).sum()
    age_greater_85_over_all = ((df_over_all['age_in_years_num']).ge(85)).sum()

    trace1 = go.Bar(
        x=['0-9', '10-17', '18-34', '35-44', '45-54', '55-64', '65-74', '75-84', '>=85'],
        y=[age_until_9_over_all, age_until_17_over_all, age_until_34_over_all, age_until_44_over_all,
           age_until_54_over_all, age_until_64_over_all, age_until_74_over_all,
           age_until_84_over_all,
           age_greater_85_over_all],
        name='Grundgesamtheit',
        marker=dict(
            color=['#E8F5AC', '#E8F5AC', '#E8F5AC', '#E8F5AC', '#E8F5AC', '#E8F5AC', '#E8F5AC', '#E8F5AC',
                  '#E8F5AC'],
            line=dict(color='#a3a3c2', width=2)))

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

    trace2 = go.Bar(
        x=['0-9', '10-17', '18-34', '35-44', '45-54', '55-64', '65-74', '75-84', '>=85'],
        y=[age_until_9, age_until_17, age_until_34, age_until_44, age_until_54, age_until_64, age_until_74,
           age_until_84,
           age_greater_85],
        name='Aktuelle Kohorte',
        marker=dict(
            color=['#32544D', '#32544D', '#32544D', '#32544D', '#32544D', '#32544D', '#32544D', '#32544D',
                   '#32544D'],
            line=dict(color='#a3a3c2', width=2)))
    return {
        'data': [trace1, trace2],

        'layout': go.Layout(
            barmode='group',
            title='Altersverteilung',
        )
    }
