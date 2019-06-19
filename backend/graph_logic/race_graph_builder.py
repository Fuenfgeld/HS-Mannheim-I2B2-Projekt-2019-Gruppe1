import plotly.graph_objs as go
from backend.data_frame_logic import data_frame_logic


def build_race_graph(queryBarLogicObject):
    df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'race_cd')
    count_white = df_patients.race_cd.str.count('white').sum()
    count_asian = df_patients.race_cd.str.count('asian').sum()
    count_black = df_patients.race_cd.str.count('black').sum()
    count_hispanic = df_patients.race_cd.str.count('hispanic').sum()
    count_indian = df_patients.race_cd.str.count('indian').sum()

    return {
        'data': [go.Pie(
            labels=['Europ.', 'Asia.', 'Afrik.', 'Hispa.', 'Indi.'],
            values=[count_white,
                    count_asian,
                    count_black,
                    count_hispanic,
                    count_indian],
            marker=dict(colors=['#4C876A', '#307087', '#32544D', '#AFD287', '#E8F5AC'],
                        line=dict(color='#a3a3c2', width=2)),
            textfont={'size': 15}
        )
        ],

        'layout': go.Layout(
            title='Ethnische Herkunft'
        )
    }
