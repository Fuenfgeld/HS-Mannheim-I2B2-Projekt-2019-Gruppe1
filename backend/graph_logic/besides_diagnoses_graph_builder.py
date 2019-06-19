import plotly.graph_objs as go
import plotly.plotly as py
import pandas as pd
import colorlover as cl

from backend.data_frame_logic import data_frame_logic
from config import database


def build_besides_diagnoses_graph(queryBarLogicObject):
    df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'concept_cd')

    diag_name = df_patients['concept_cd'].value_counts().keys().to_list()
    diag_num = df_patients['concept_cd'].value_counts().tolist()

    string_name1 = f'select distinct c_name from i2b2metadata.icd10_icd9 where c_basecode = \'{diag_name[0]}\''
    string_name2 = f'select distinct c_name from i2b2metadata.icd10_icd9 where c_basecode = \'{diag_name[1]}\''
    string_name3 = f'select distinct c_name from i2b2metadata.icd10_icd9 where c_basecode = \'{diag_name[2]}\''
    string_name4 = f'select distinct c_name from i2b2metadata.icd10_icd9 where c_basecode = \'{diag_name[3]}\''
    string_name5 = f'select distinct c_name from i2b2metadata.icd10_icd9 where c_basecode = \'{diag_name[4]}\''

    name1_df = pd.read_sql(string_name1, con=database.engine)
    name2_df = pd.read_sql(string_name2, con=database.engine)
    name3_df = pd.read_sql(string_name3, con=database.engine)
    name4_df = pd.read_sql(string_name4, con=database.engine)
    name5_df = pd.read_sql(string_name5, con=database.engine)

    number1 = diag_num[0]
    number2 = diag_num[1]
    number3 = diag_num[2]
    number4 = diag_num[3]
    number5 = diag_num[4]

    name1 = name1_df.loc[0].values[0]
    name2 = name2_df.loc[0].values[0]
    name3 = name3_df.loc[0].values[0]
    name4 = name4_df.loc[0].values[0]
    name5 = name5_df.loc[0].values[0]

    trace = go.Bar(
        x=[number1, number2, number3, number4, number5],
        y=[f'\'{name1}\'', f'\'{name2}\'', f'\'{name3}\'', f'\'{name4}\'',
           f'\'{name5}\''],

        orientation='h',
        marker=dict(
            color=['#4C876A', '#307087', '#32544D', '#AFD287', '#E8F5AC'],
            line=dict(color='#a3a3c2', width=2),



        )

    )

    return {
        'data': [trace],
        'layout': go.Layout(
            title='Nebendiagnosen',
            xaxis={},
            yaxis=go.layout.YAxis(
                    font=dict(size=80)
                )

        ),

    }
