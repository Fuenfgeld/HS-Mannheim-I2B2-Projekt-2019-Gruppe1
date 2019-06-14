import dash
import dash_html_components as html

from backend.data_frame_logic import data_frame_logic
from backend.query_bar_logic import query_bar_logic
queryBarLogicObject = query_bar_logic.queryBar()


class AbfrageleisteCcallback:

    def deci(self, value):
        df_code = data_frame_logic.generate_df_icd_code(queryBarLogicObject, value)
        queryBarLogicObject.append_icd_list_decimal(df_code.loc[0].values[0])
        df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'decimal')
        count_patients = len(df_patients)
        return count_patients