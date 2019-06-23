import plotly.graph_objs as go
from backend.data_frame_logic import data_frame_logic_new


def build_age_graph(queryBarLogicNewObject, resultMergeObject):
    df_over_all = resultMergeObject.df_age_in_years_num
    df_patients = data_frame_logic_new.generate_df_all_patients(queryBarLogicNewObject, resultMergeObject,
                                                                'age_in_years_num')

    if len(df_patients) == 0:
        return {}

    age_until_9_over_all = (
                ((df_over_all['age_in_years_num']).ge(0)) & ((df_over_all['age_in_years_num']).le(10))).sum()
    age_until_17_over_all = (
            ((df_over_all['age_in_years_num']).ge(10)) & ((df_over_all['age_in_years_num']).le(20))).sum()
    age_until_34_over_all = (
            ((df_over_all['age_in_years_num']).ge(20)) & ((df_over_all['age_in_years_num']).le(30))).sum()
    age_until_44_over_all = (
            ((df_over_all['age_in_years_num']).ge(30)) & ((df_over_all['age_in_years_num']).le(40))).sum()
    age_until_54_over_all = (
            ((df_over_all['age_in_years_num']).ge(40)) & ((df_over_all['age_in_years_num']).le(50))).sum()
    age_until_64_over_all = (
            ((df_over_all['age_in_years_num']).ge(50)) & ((df_over_all['age_in_years_num']).le(60))).sum()
    age_until_74_over_all = (
            ((df_over_all['age_in_years_num']).ge(60)) & ((df_over_all['age_in_years_num']).le(70))).sum()
    age_until_84_over_all = (
            ((df_over_all['age_in_years_num']).ge(70)) & ((df_over_all['age_in_years_num']).le(80))).sum()
    age_greater_85_over_all = ((df_over_all['age_in_years_num']).ge(80)).sum()
    trace1 = go.Bar(
        x=['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '>=80'],
        y=[age_until_9_over_all, age_until_17_over_all, age_until_34_over_all, age_until_44_over_all,
           age_until_54_over_all, age_until_64_over_all, age_until_74_over_all,
           age_until_84_over_all,
           age_greater_85_over_all],
        name='Grundgesamtheit',
        marker=dict(
            color=['#E8F5AC', '#E8F5AC', '#E8F5AC', '#E8F5AC', '#E8F5AC', '#E8F5AC', '#E8F5AC', '#E8F5AC',
                   '#E8F5AC'],
            line=dict(color='#a3a3c2', width=0.5)
        ))

    age_until_9 = (((df_patients['age_in_years_num']).ge(0)) & ((df_patients['age_in_years_num']).le(10))).sum()
    age_until_17 = (((df_patients['age_in_years_num']).ge(10)) & ((df_patients['age_in_years_num']).le(20))).sum()
    age_until_34 = (((df_patients['age_in_years_num']).ge(20)) & ((df_patients['age_in_years_num']).le(30))).sum()
    age_until_44 = (((df_patients['age_in_years_num']).ge(30)) & ((df_patients['age_in_years_num']).le(40))).sum()
    age_until_54 = (((df_patients['age_in_years_num']).ge(40)) & ((df_patients['age_in_years_num']).le(50))).sum()
    age_until_64 = (((df_patients['age_in_years_num']).ge(50)) & ((df_patients['age_in_years_num']).le(60))).sum()
    age_until_74 = (((df_patients['age_in_years_num']).ge(60)) & ((df_patients['age_in_years_num']).le(70))).sum()
    age_until_84 = (((df_patients['age_in_years_num']).ge(70)) & ((df_patients['age_in_years_num']).le(80))).sum()
    age_greater_85 = ((df_patients['age_in_years_num']).ge(80)).sum()
    trace2 = go.Bar(
        x=['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '>=80'],
        y=[age_until_9, age_until_17, age_until_34, age_until_44, age_until_54, age_until_64, age_until_74,
           age_until_84,
           age_greater_85],
        name='Aktuelle Kohorte',
        marker=dict(
            color=['#32544D', '#32544D', '#32544D', '#32544D', '#32544D', '#32544D', '#32544D', '#32544D',
                   '#32544D'],
            line=dict(color='#a3a3c2', width=0.5)
        ))

    return {
        'data': [trace1, trace2],

        'layout': go.Layout(
            barmode='relative',
            title='Altersverteilung',
            xaxis=dict(
                title='Jahre',
            ),
            yaxis=dict(
                title='Anzahl',
            ),
            legend=dict(
                x=0.6,
                y=1.0,
            ),
        )

    }
