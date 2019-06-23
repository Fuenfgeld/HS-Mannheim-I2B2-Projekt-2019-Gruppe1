import plotly.graph_objs as go
from backend.data_frame_logic import data_frame_logic_new


def build_language_graph(queryBarLogicNewObject, resultMergeObject):
    df_patients_all = resultMergeObject.df_language_cd
    df_patients = data_frame_logic_new.generate_df_all_patients(queryBarLogicNewObject, resultMergeObject,
                                                                'language_cd')

    if len(df_patients) == 0:
        return {}

    count_english_all = df_patients_all.language_cd.str.count('english').sum()
    count_spanish_all = df_patients_all.language_cd.str.count('spanish').sum()
    count_german_all = df_patients_all.language_cd.str.count('german').sum()
    trace1 = go.Pie(
        labels=['Englisch', 'Spanisch', 'Deutsch'],
        values=[count_english_all, count_spanish_all, count_german_all],
        textposition='inside',
        domain={'x': [0.20, 0.80], 'y': [0.20, 0.80]},
        marker=dict(
            colors=['#32544D', '#E8F5AC', '#AFD287'],
            line=dict(color='#a3a3c2', width=0.5)))

    count_english = df_patients.language_cd.str.count('english').sum()
    count_spanish = df_patients.language_cd.str.count('spanish').sum()
    count_german = df_patients.language_cd.str.count('german').sum()
    trace2 = go.Pie(
        labels=['Englisch', 'Spanisch', 'Deutsch'],
        values=[count_english, count_spanish, count_german],
        textposition='outside',
        hole=0.7,
        marker=dict(
            colors=['#32544D', '#E8F5AC', '#AFD287'],
            line=dict(color='#a3a3c2', width=0.5)))

    return {
        'data': [trace1, trace2],
        'layout': go.Layout(
            title='Muttersprache',
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
