import unittest


class testDataFrameLogic(unittest.TestCase):

    def test_generate_df_all_patient(self):
        import deprecated.data_frame_logic as dfl
        from deprecated import query_bar_logic
        queryBarObject = query_bar_logic.queryBar()

        self.assertEqual(dfl.generate_df_all_patients(queryBarObject, 'dezimal'), None)
        self.assertEqual(len(dfl.generate_df_all_patients(queryBarObject, 'decimal')), 134)
        self.assertEqual(len(dfl.generate_df_all_patients(queryBarObject, 'sex_cd')), 134)
        self.assertEqual(len(dfl.generate_df_all_patients(queryBarObject, 'language_cd')), 134)
        self.assertEqual(len(dfl.generate_df_all_patients(queryBarObject, 'age_in_years_num')), 134)
        self.assertEqual(len(dfl.generate_df_all_patients(queryBarObject, 'race_cd')), 134)
        self.assertEqual(len(dfl.generate_df_all_patients(queryBarObject, 'income_cd')), 134)



    def test_generate_df_icd_code(self):
        import deprecated.data_frame_logic as dfl
        from deprecated import query_bar_logic
        queryBarObject = query_bar_logic.queryBar()

        self.assertEqual(len(dfl.generate_df_icd_code(queryBarObject, 'Lumbago')), 1)
        self.assertIsInstance(len(dfl.generate_df_icd_code(queryBarObject, 'Lumbago')), int)


    def test_generate_df_sex_cd_patients_dimension(self):
        import deprecated.data_frame_logic as dfl

        self.assertEqual(len(dfl.generate_df_sex_cd_patient_dimension()), 134)
        self.assertIsInstance(len(dfl.generate_df_sex_cd_patient_dimension()), int)


    def test_generate_df_language_cd_patient_dimension(self):
        import deprecated.data_frame_logic as dfl

        self.assertEqual(len(dfl.generate_df_language_cd_patient_dimension()), 134)
        self.assertIsInstance(len(dfl.generate_df_language_cd_patient_dimension()), int)


    def test_generate_df_age_in_year_num_patient_dimension(self):
        import deprecated.data_frame_logic as dfl

        self.assertEqual(len(dfl.generate_df_age_in_years_num_patient_dimension()), 134)
        self.assertIsInstance(len(dfl.generate_df_age_in_years_num_patient_dimension()), int)

    def test_generate_df_race_cd_patient_dimension(self):
        import deprecated.data_frame_logic as dfl

        self.assertEqual(len(dfl.generate_df_race_cd_patient_dimension()), 134)
        self.assertIsInstance(len(dfl.generate_df_race_cd_patient_dimension()), int)

    def test_generate_df_income_cd_patient_dimension(self):
        import deprecated.data_frame_logic as dfl

        self.assertEqual(len(dfl.generate_df_income_cd_patient_dimension()), 134)
        self.assertIsInstance(len(dfl.generate_df_income_cd_patient_dimension()), int)

    def test_generate_df_diag_all_observation_fact_number(self):
        import deprecated.data_frame_logic as dfl

        self.assertEqual(len(dfl.generate_df_diag_all_observation_fact_number()), 10)
        self.assertIsInstance(len(dfl.generate_df_diag_all_observation_fact_number()), int)

    def test_generate_df_diag_all_observation_fact_icd(self):
        import deprecated.data_frame_logic as dfl

        self.assertEqual(len(dfl.generate_df_diag_all_observation_fact_icd()), 10)
        self.assertIsInstance(len(dfl.generate_df_diag_all_observation_fact_icd()), int)