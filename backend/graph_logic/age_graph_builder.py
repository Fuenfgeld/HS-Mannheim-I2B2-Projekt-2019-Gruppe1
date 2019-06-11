import plotly.graph_objs as go


def build_age_graph(df_patients):
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
                color=['#32544D', '#32544D', '#32544D', '#32544D', '#32544D', '#32544D', '#32544D', '#32544D',
                       '#32544D'],
                line=dict(color='#a3a3c2', width=2)),
        ),
        ],

        'layout': go.Layout(
            title='Altersverteilung',
        )
    }
