import pandas as pd
from backend.data_frame_logic import data_frame_logic_new


class resultMerge:

    def __init__(self):
        self.df_sex_cd = data_frame_logic_new.generate_df_sex_cd_patient_dimension()
        self.df_language_cd = data_frame_logic_new.generate_df_language_cd_patient_dimension()
        self.df_age_in_years_num = data_frame_logic_new.generate_df_age_in_years_num_patient_dimension()
        self.df_race_cd = data_frame_logic_new.generate_df_race_cd_patient_dimension()
        self.df_income_cd = data_frame_logic_new.generate_df_income_cd_patient_dimension()
        self.df_concept_cd = data_frame_logic_new.generate_df_only_pat_num()

    def merge_two_df(self, df, case):
        if case == 'sex_cd':
            return pd.merge(df, self.df_sex_cd, how='inner', on='patient_num')
        elif case == 'language_cd':
            return pd.merge(df, self.df_language_cd, how='inner', on='patient_num')
        elif case == 'age_in_years_num':
            return pd.merge(df, self.df_age_in_years_num, how='inner', on='patient_num')
        elif case == 'race_cd':
            return pd.merge(df, self.df_race_cd, how='inner', on='patient_num')
        elif case == 'income_cd':
            return pd.merge(df, self.df_income_cd, how='inner', on='patient_num')
        elif case == 'concept_cd':
            return pd.merge(df, self.df_concept_cd, how='inner', on='patient_num')