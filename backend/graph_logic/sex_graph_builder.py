import plotly.graph_objs as go


def build_sex_graph(df_patients):
    count_male = df_patients.sex_cd.str.count('M').sum()
    count_female = df_patients.sex_cd.str.count('F').sum()
    return {
        'data': [go.Pie(
            labels=['Weiblich', 'Männlich'],
            values=[count_female,
                    count_male],
            marker=dict(colors=['#32544D', '#AFD287'],
                        line=dict(color='#a3a3c2', width=2)),
            textfont={'size': 15},
            textinfo='value'
        )
        ],

        'layout': go.Layout(
            title='Geschlechterverteilung'
        )
    }
