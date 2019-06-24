import plotly.graph_objs as go
from backend.data_frame_logic import data_frame_logic_new


def build_sex_graph(queryBarLogicNewObject, resultMergeObject):
    df_patients = data_frame_logic_new.generate_df_all_patients(queryBarLogicNewObject, resultMergeObject, 'sex_cd')

    if len(df_patients) == 0:
        return {}

    count_male = df_patients.sex_cd.str.count('M').sum()
    count_female = df_patients.sex_cd.str.count('F').sum()

    return {
        'data': [go.Pie(
            labels=['Weiblich', 'Männlich'],
            values=[count_female,
                    count_male],
            marker=dict(colors=['#32544D', '#AFD287'],
                        line=dict(color='#a3a3c2', width=0.5)),
            textfont={'size': 15},
            textposition='outside',
            hoverinfo='label+value',
            hole=.3
        )
        ],

        'layout': go.Layout(
            legend=dict(
                x=0,
                y=1.0,
            ),
            annotations=[
                dict(
                    font={'size': 16},
                    showarrow=False,
                    text="♀♂",
                    x=0.50,
                    y=0.5
                )
            ]
        )
    }
