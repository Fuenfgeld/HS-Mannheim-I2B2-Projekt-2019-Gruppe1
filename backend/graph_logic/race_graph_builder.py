import plotly.graph_objs as go
from backend.data_frame_logic import data_frame_logic_new


def build_race_graph(queryBarLogicNewObject, resultMergeObject):
    df_over_all = resultMergeObject.df_race_cd
    df_patients = data_frame_logic_new.generate_df_all_patients(queryBarLogicNewObject, resultMergeObject, 'race_cd')

    if len(df_patients) == 0:
        return {}

    count_white_over_all = df_over_all.race_cd.str.count('white').sum()
    count_asian_over_all = df_over_all.race_cd.str.count('asian').sum()
    count_black_over_all = df_over_all.race_cd.str.count('black').sum()
    count_hispanic_over_all = df_over_all.race_cd.str.count('hispanic').sum()
    count_indian_over_all = df_over_all.race_cd.str.count('indian').sum()
    trace1 = go.Bar(
        x=['European', 'Asian', 'African', 'Hispanic', 'Indian'],
        y=[count_white_over_all,
           count_asian_over_all,
           count_black_over_all,
           count_hispanic_over_all,
           count_indian_over_all],
        name='Basic population',
        marker=dict(color=['#1d344d', '#1d344d', '#1d344d', '#1d344d', '#1d344d'],
                    line=dict(color='#a3a3c2', width=0.5)),
    )

    count_white = df_patients.race_cd.str.count('white').sum()
    count_asian = df_patients.race_cd.str.count('asian').sum()
    count_black = df_patients.race_cd.str.count('black').sum()
    count_hispanic = df_patients.race_cd.str.count('hispanic').sum()
    count_indian = df_patients.race_cd.str.count('indian').sum()
    trace2 = go.Bar(
        x=['European', 'Asian', 'African', 'Hispanic', 'Indian'],
        y=[count_white,
           count_asian,
           count_black,
           count_hispanic,
           count_indian],
        name='Selected cohort',
        marker=dict(color=['#b0d18a', '#b0d18a', '#b0d18a', '#b0d18a', '#b0d18a'],
                    line=dict(color='#a3a3c2', width=0.5)),
    )

    return {
        'data': [trace1, trace2],

        'layout': go.Layout(
            title='Ethnic origin',
            bargroupgap=0.1,
            legend=dict(
                x=0.8,
                y=1.0,
            ),
            yaxis=dict(
                title='Number of patients',
            ),
        )
    }
