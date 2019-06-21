import plotly.graph_objs as go
from backend.data_frame_logic import data_frame_logic


def build_income_graph(queryBarLogicObject):
    df_patients_all = data_frame_logic.generate_df_income_cd_patient_dimension()
    income1_all = df_patients_all.income_cd.str.count('Low').sum()
    income2_all = df_patients_all.income_cd.str.count('Medium').sum()
    income3_all = df_patients_all.income_cd.str.count('High').sum()

    trace1 = go.Bar(
        x=['Niedrig', 'Mittel', 'Hoch'],
        y=[income1_all, income2_all, income3_all],
        name='Gesamt',
        marker=dict(
            color=['#E8F5AC', '#E8F5AC', '#E8F5AC'],
            line=dict(color='#a3a3c2', width=2)))

    df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'income_cd')
    income1 = df_patients.income_cd.str.count('Low').sum()
    income2 = df_patients.income_cd.str.count('Medium').sum()
    income3 = df_patients.income_cd.str.count('High').sum()

    trace2 = go.Bar(
        x=['Niedrig', 'Mittel', 'Hoch'],
        y=[income1, income2, income3],
        name='Kohorte',
        marker=dict(
            color=['#32544D', '#32544D', '#32544D'],
            line=dict(color='#a3a3c2', width=2),

            ))

    return {
        'data': [trace1, trace2],

        'layout': go.Layout(
            barmode='group',
            title='Einkommen',

        )
    }
