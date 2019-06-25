from backend.data_frame_logic import data_frame_logic_new
import dash_html_components as html


def build_decimal(queryBarLogicNewObject, resultMergeObject):
    df_patients = data_frame_logic_new.generate_df_all_patients(queryBarLogicNewObject, resultMergeObject, 'decimal')
    count_patients = len(df_patients)
    return html.H5('Patients: ' + str(count_patients))