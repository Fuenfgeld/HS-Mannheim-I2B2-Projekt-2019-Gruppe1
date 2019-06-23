from backend.data_frame_logic import data_frame_logic
import dash_html_components as html


def build_decimal(queryBarLogicObject):
    df_patients = data_frame_logic.generate_df_all_patients(queryBarLogicObject, 'decimal')
    count_patients = len(df_patients)
    return html.H5('Anzahl Patienten: ' + str(count_patients))