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
            ((df_over_all['age_in_years_num']).ge(11)) & ((df_over_all['age_in_years_num']).le(20))).sum()
    age_until_34_over_all = (
            ((df_over_all['age_in_years_num']).ge(21)) & ((df_over_all['age_in_years_num']).le(30))).sum()
    age_until_44_over_all = (
            ((df_over_all['age_in_years_num']).ge(31)) & ((df_over_all['age_in_years_num']).le(40))).sum()
    age_until_54_over_all = (
            ((df_over_all['age_in_years_num']).ge(41)) & ((df_over_all['age_in_years_num']).le(50))).sum()
    age_until_64_over_all = (
            ((df_over_all['age_in_years_num']).ge(51)) & ((df_over_all['age_in_years_num']).le(60))).sum()
    age_until_74_over_all = (
            ((df_over_all['age_in_years_num']).ge(61)) & ((df_over_all['age_in_years_num']).le(70))).sum()
    age_until_84_over_all = (
            ((df_over_all['age_in_years_num']).ge(71)) & ((df_over_all['age_in_years_num']).le(80))).sum()
    age_greater_85_over_all = ((df_over_all['age_in_years_num']).ge(81)).sum()
    trace1 = go.Bar(
        x=['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '>80'],
        y=[age_until_9_over_all, age_until_17_over_all, age_until_34_over_all, age_until_44_over_all,
           age_until_54_over_all, age_until_64_over_all, age_until_74_over_all,
           age_until_84_over_all,
           age_greater_85_over_all],
        name='Basic population',
        marker=dict(
            color=['#1d344d', '#1d3441', '#1d3441', '#1d3441', '#1d3441', '#1d3441', '#1d3441', '#1d3441',
                   '#1d3441'],
            line=dict(color='#a3a3c2', width=0.5)
        ))

    age_until_9 = (((df_patients['age_in_years_num']).ge(0)) & ((df_patients['age_in_years_num']).le(10))).sum()
    age_until_17 = (((df_patients['age_in_years_num']).ge(11)) & ((df_patients['age_in_years_num']).le(20))).sum()
    age_until_34 = (((df_patients['age_in_years_num']).ge(21)) & ((df_patients['age_in_years_num']).le(30))).sum()
    age_until_44 = (((df_patients['age_in_years_num']).ge(31)) & ((df_patients['age_in_years_num']).le(40))).sum()
    age_until_54 = (((df_patients['age_in_years_num']).ge(41)) & ((df_patients['age_in_years_num']).le(50))).sum()
    age_until_64 = (((df_patients['age_in_years_num']).ge(51)) & ((df_patients['age_in_years_num']).le(60))).sum()
    age_until_74 = (((df_patients['age_in_years_num']).ge(61)) & ((df_patients['age_in_years_num']).le(70))).sum()
    age_until_84 = (((df_patients['age_in_years_num']).ge(71)) & ((df_patients['age_in_years_num']).le(80))).sum()
    age_greater_85 = ((df_patients['age_in_years_num']).ge(81)).sum()
    trace2 = go.Bar(
        x=['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '>80'],
        y=[age_until_9, age_until_17, age_until_34, age_until_44, age_until_54, age_until_64, age_until_74,
           age_until_84,
           age_greater_85],
        name='Selected cohort',
        marker=dict(
            color=['#b0d18a', '#b0d18a', '#b0d18a', '#b0d18a', '#b0d18a', '#b0d18a', '#b0d18a', '#b0d18a',
                   '#b0d18a'], ##32544D
            line=dict(color='#a3a3c2', width=0.5)
        ))

    return {
        'data': [trace1, trace2],

        'layout': go.Layout(
            barmode='relative',
            title='Age',
            xaxis=dict(
                title='Years',
            ),
            yaxis=dict(
                title='Number of patients',
            ),
            legend=dict(
                x=0.6,
                y=1.0,
            ),
        )

    }
