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
        labels=['Niedrig', 'Mittel', 'Hoch'],
        values=[income1_all, income2_all, income3_all],
        textposition='inside',
        domain={'x': [0.20, 0.80], 'y': [0.20, 0.80]},
        marker=dict(
            colors=['#32544D', '#E8F5AC', '#AFD287'],
            line=dict(color='#a3a3c2', width=0.5)))

    income1 = df_patients.income_cd.str.count('Low').sum()
    income2 = df_patients.income_cd.str.count('Medium').sum()
    income3 = df_patients.income_cd.str.count('High').sum()
    trace2 = go.Pie(
        labels=['Niedrig', 'Mittel', 'Hoch'],
        values=[income1, income2, income3],
        textposition='outside',
        hole=0.7,
        marker=dict(
            colors=['#32544D', '#E8F5AC', '#AFD287'],
            line=dict(color='#a3a3c2', width=0.5),

        ))

    return {
        'data': [trace1, trace2],
        'layout': go.Layout(
            title='Einkommen',
            annotations=[
                dict(
                    font={'size': 12},
                    showarrow=False,
                    text="Innen: Grundgesamtheit",
                    x=0.50,
                    y=0
                ),
                dict(
                    font={'size': 12},
                    showarrow=False,
                    text="Außen: Aktuelle Kohorte",
                    x=0.50,
                    y=-0.1
                )
            ]
        )
    }


