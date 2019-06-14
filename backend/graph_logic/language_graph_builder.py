import plotly.graph_objs as go
from backend.data_frame_logic import data_frame_logic


def build_language_graph(queryBarLogicObject):
    df_patients_all = data_frame_logic.generate_df_language_cd_patient_dimension()
    count_english_all = df_patients_all.language_cd.str.count('english').sum()
    count_spanish_all = df_patients_all.language_cd.str.count('spanish').sum()
    count_german_all = df_patients_all.language_cd.str.count('german').sum()

    trace1 = go.Bar(
        x=['Englisch', 'Spansich', 'Deutsch'],
        y=[count_english_all, count_spanish_all, count_german_all],
        name='Grundgesamtheit',
        marker=dict(
            color=['#E8F5AC', '#E8F5AC', '#E8F5AC'],
            line=dict(color='#a3a3c2', width=2)))

    df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'language_cd')
    count_english = df_patients.language_cd.str.count('english').sum()
    count_spanish = df_patients.language_cd.str.count('spanish').sum()
    count_german = df_patients.language_cd.str.count('german').sum()
    trace2 = go.Bar(
        x=['Englisch', 'Spansich', 'Deutsch'],
        y=[count_english, count_spanish, count_german],
        name='Aktuelle Kohorte',
        marker=dict(
            color=['#32544D', '#32544D', '#32544D'],
            line=dict(color='#a3a3c2', width=2)))

    return {
        'data': [trace1, trace2],

        'layout': go.Layout(
            barmode='group',
            title='Verteilung nach Muttersprache',
        )}
