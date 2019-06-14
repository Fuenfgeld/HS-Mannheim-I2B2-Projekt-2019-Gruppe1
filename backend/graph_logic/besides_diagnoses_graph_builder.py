import plotly.graph_objs as go
from backend.data_frame_logic import data_frame_logic
import pandas as pd
from config import database

def build_besides_diagnoses_graph(queryBarLogicObject):
    df_diag_num = data_frame_logic.generate_df_diag_all_observatio_fact_number()

    df_diag_icd = data_frame_logic.generate_df_diag_all_observatio_fact_icd()

    df_diag_icd_name = pd.read_sql('select distinct c_basecode as concept_cd, c_name from i2b2.i2b2metadata.icd10_icd9', con=database.engine)

    df_10_icd_name = pd.merge(df_diag_icd, df_diag_icd_name, how='inner', on='concept_cd')

    print(df_10_icd_name)
    print(df_diag_num)

    name1 = df_10_icd_name.loc[0].values[1]
    name2 = df_10_icd_name.loc[1].values[1]
    name3 = df_10_icd_name.loc[2].values[1]

    number1 = df_diag_num.loc[0].values[0]
    number2 = df_diag_num.loc[1].values[0]
    number3 = df_diag_num.loc[2].values[0]

    trace1 = go.Bar(
        y=[number1, number2, number3],
        x=[name1, name2, name3],
        name='Aktuelle Kohorte',
        marker=dict(
            color=['#E8F5AC', '#E8F5AC', '#E8F5AC'],
            line=dict(color='#a3a3c2', width=2)))

    return {
        'data': [trace1],

        'layout': go.Layout(
            barmode='group',
            title='Einkommen-Verteilung',
        )
    }