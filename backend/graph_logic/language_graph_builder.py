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
        labels=['English', 'Spanish', 'German'],
        values=[count_english_all, count_spanish_all, count_german_all],
        textposition='inside',
        name='Basic population',
        domain={'x': [0.20, 0.80], 'y': [0.20, 0.80]},
        marker=dict(
            colors=['#e5f4b0', '#81b1b1', '#bfdbaa'],
            line=dict(color='#a3a3c2', width=0.5)))

    count_english = df_patients.language_cd.str.count('english').sum()
    count_spanish = df_patients.language_cd.str.count('spanish').sum()
    count_german = df_patients.language_cd.str.count('german').sum()
    trace2 = go.Pie(
        labels=['English', 'Spanish', 'German'],
        values=[count_english, count_spanish, count_german],
        textposition='outside',
        name='Selected cohort',
        hole=0.7,
        marker=dict(
            colors=['#e5f4b0', '#81b1b1', '#bfdbaa'],
            line=dict(color='#a3a3c2', width=0.5)))

    return {
        'data': [trace1, trace2],
        'layout': go.Layout(
            title='Language',
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
