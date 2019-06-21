import plotly.graph_objs as go
from backend.data_frame_logic import data_frame_logic


def build_sex_graph(queryBarLogicObject):
    df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'sex_cd')
    count_male = df_patients.sex_cd.str.count('M').sum()
    count_female = df_patients.sex_cd.str.count('F').sum()


    return {
        'data': [go.Pie(
            labels=['Weib.', 'Männ.'],
            values=[count_female,
                    count_male],
            marker=dict(colors=['#32544D', '#AFD287'],
                        line=dict(color='#a3a3c2', width=2)),
            textfont={'size': 15},
        )
        ],

        'layout': go.Layout(
            title='Geschlecht'
        )
    }
