import plotly.graph_objs as go
from backend.data_frame_logic import data_frame_logic_new


def build_income_graph(queryBarLogicNewObject, resultMergeObject):
    df_patients_all = resultMergeObject.df_income_cd
    df_patients = data_frame_logic_new.generate_df_all_patients(queryBarLogicNewObject, resultMergeObject, 'income_cd')

    if len(df_patients) == 0:
        return {}

    income1_all = df_patients_all.income_cd.str.count('Low').sum()
    income2_all = df_patients_all.income_cd.str.count('Medium').sum()
    income3_all = df_patients_all.income_cd.str.count('High').sum()
    trace1 = go.Pie(
        labels=['Low', 'Medium', 'High'],
        values=[income1_all, income2_all, income3_all],
        textposition='inside',
        domain={'x': [0.20, 0.80], 'y': [0.20, 0.80]},
        marker=dict(
            colors=['#2e7d7c', '#c6df76', '#93c371'],
            line=dict(color='#a3a3c2', width=0.5)))

    income1 = df_patients.income_cd.str.count('Low').sum()
    income2 = df_patients.income_cd.str.count('Medium').sum()
    income3 = df_patients.income_cd.str.count('High').sum()
    trace2 = go.Pie(
        labels=['Low', 'Medium', 'High'],
        values=[income1, income2, income3],
        textposition='outside',
        hole=0.7,
        marker=dict(
            colors=['#2e7d7c', '#c6df76', '#93c371'],
            line=dict(color='#a3a3c2', width=0.5),

        ))

    return {
        'data': [trace1, trace2],
        'layout': go.Layout(
            title='Income',
            annotations=[
                dict(
                    font={'size': 12},
                    showarrow=False,
                    text="Inside: Basic population",
                    x=0.50,
                    y=0
                ),
                dict(
                    font={'size': 12},
                    showarrow=False,
                    text="Outside: Selected cohort",
                    x=0.50,
                    y=-0.1
                )
            ]
        )
    }


