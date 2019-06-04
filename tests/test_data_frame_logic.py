import unittest


class testDataFrameLogic(unittest.TestCase):

    def test_generate_df_all_patient(self):
        import backend.data_frame_logic.data_frame_logic as dfl
        from backend.query_bar_logic import query_bar_logic
        queryBarObject = query_bar_logic.queryBar()

        self.assertEqual(dfl.generate_df_all_patients(queryBarObject, 'dezimal'), None)
        self.assertEqual(len(dfl.generate_df_all_patients(queryBarObject, 'sex_cd')), 134)
        self.assertEqual(len(dfl.generate_df_all_patients(queryBarObject, 'language_cd')), 134)
        self.assertEqual(len(dfl.generate_df_all_patients(queryBarObject, 'age_in_years_num')), 134)


    def test_generate_df_icd_code(self):
        import backend.data_frame_logic.data_frame_logic as dfl
        from backend.query_bar_logic import query_bar_logic
        queryBarObject = query_bar_logic.queryBar()

        self.assertEqual(len(dfl.generate_df_icd_code(queryBarObject, 'Lumbago')), 1)
        self.assertIsInstance(len(dfl.generate_df_icd_code(queryBarObject, 'Lumbago')), int)


    def test_generate_df_sex_cd_patients_dimension(self):
        import backend.data_frame_logic.data_frame_logic as dfl

        self.assertEqual(len(dfl.generate_df_sex_cd_patient_dimension()), 134)
        self.assertIsInstance(len(dfl.generate_df_sex_cd_patient_dimension()), int)


    def test_generate_df_language_cd_patient_dimension(self):
        import backend.data_frame_logic.data_frame_logic as dfl

        self.assertEqual(len(dfl.generate_df_language_cd_patient_dimension()), 134)
        self.assertIsInstance(len(dfl.generate_df_language_cd_patient_dimension()), int)


    def test_generate_df_age_in_year_num_patient_dimension(self):
        import backend.data_frame_logic.data_frame_logic as dfl

        self.assertEqual(len(dfl.generate_df_age_in_years_num_patient_dimension()), 134)
        self.assertIsInstance(len(dfl.generate_df_age_in_years_num_patient_dimension()), int)