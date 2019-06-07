import pandas as pd
from backend.data_frame_logic import data_frame_logic


def merge_two_df(df, case):
    if case == 'sex_cd':
        return pd.merge(df, data_frame_logic.generate_df_sex_cd_patient_dimension(), how='inner', on='patient_num')
    elif case == 'language_cd':
        return pd.merge(df, data_frame_logic.generate_df_language_cd_patient_dimension(), how='inner', on='patient_num')
    elif case == 'age_in_years_num':
        return pd.merge(df, data_frame_logic.generate_df_age_in_years_num_patient_dimension(), how='inner', on='patient_num')
    elif case == 'race_cd':
        return  pd.merge(df, data_frame_logic.generate_df_race_cd_patient_dimension(), how='inner', on='patient_num')