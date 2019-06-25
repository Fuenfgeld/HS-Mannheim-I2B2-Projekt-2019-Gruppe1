import unittest


class testDataFrameLogic(unittest.TestCase):

    def test_generate_df_default(self):
        from backend.data_frame_logic import data_frame_logic_new

        self.assertEqual(len(data_frame_logic_new.generate_df_default()), 134)
        self.assertIsInstance(len(data_frame_logic_new.generate_df_default()), int)

    def test_generate_df_two_criteria(self):
        from backend.data_frame_logic import data_frame_logic_new
        from backend.query_bar_logic import query_bar_logic_new
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()

        queryBarLogicObject.append_selection('Lumbago')
        queryBarLogicObject.append_selection('Bronchiectasis')
        self.assertEqual(len(
            data_frame_logic_new.generate_df_two_criteria(queryBarLogicObject.con_list, queryBarLogicObject.df_list)),
                         1)
        self.assertIsInstance(len(data_frame_logic_new.generate_df_income_cd_patient_dimension()), int)

    def test_generate_df_three_criteria(self):
        from backend.data_frame_logic import data_frame_logic_new
        from backend.query_bar_logic import query_bar_logic_new
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()

        queryBarLogicObject.append_selection('Lumbago')
        queryBarLogicObject.append_selection('Bronchiectasis')
        queryBarLogicObject.append_selection('Certain infectious and parasitic diseases (a00-b99)')
        self.assertEqual(len(
            data_frame_logic_new.generate_df_three_criteria(queryBarLogicObject.con_list, queryBarLogicObject.df_list)),
                         1)
        self.assertIsInstance(len(data_frame_logic_new.generate_df_income_cd_patient_dimension()), int)

    def test_generate_df_all_patient(self):
        from backend.data_frame_logic import data_frame_logic_new
        from backend.query_bar_logic import query_bar_logic_new
        from backend.result_logic import result_merge
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()
        resultMergeObject = result_merge.resultMerge()

        self.assertEqual(
            data_frame_logic_new.generate_df_all_patients(queryBarLogicObject, resultMergeObject, 'dezimal'), None)
        self.assertEqual(
            len(data_frame_logic_new.generate_df_all_patients(queryBarLogicObject, resultMergeObject, 'decimal')), 134)
        self.assertEqual(
            len(data_frame_logic_new.generate_df_all_patients(queryBarLogicObject, resultMergeObject, 'sex_cd')), 134)
        self.assertEqual(
            len(data_frame_logic_new.generate_df_all_patients(queryBarLogicObject, resultMergeObject, 'language_cd')),
            134)
        self.assertEqual(len(
            data_frame_logic_new.generate_df_all_patients(queryBarLogicObject, resultMergeObject, 'age_in_years_num')),
            134)
        self.assertEqual(
            len(data_frame_logic_new.generate_df_all_patients(queryBarLogicObject, resultMergeObject, 'race_cd')), 134)
        self.assertEqual(
            len(data_frame_logic_new.generate_df_all_patients(queryBarLogicObject, resultMergeObject, 'income_cd')),
            134)

    def test_generate_df_sex_cd_patients_dimension(self):
        from backend.data_frame_logic import data_frame_logic_new

        self.assertEqual(len(data_frame_logic_new.generate_df_sex_cd_patient_dimension()), 134)
        self.assertIsInstance(len(data_frame_logic_new.generate_df_sex_cd_patient_dimension()), int)

    def test_generate_df_language_cd_patient_dimension(self):
        from backend.data_frame_logic import data_frame_logic_new

        self.assertEqual(len(data_frame_logic_new.generate_df_language_cd_patient_dimension()), 134)
        self.assertIsInstance(len(data_frame_logic_new.generate_df_language_cd_patient_dimension()), int)

    def test_generate_df_age_in_year_num_patient_dimension(self):
        from backend.data_frame_logic import data_frame_logic_new

        self.assertEqual(len(data_frame_logic_new.generate_df_age_in_years_num_patient_dimension()), 134)
        self.assertIsInstance(len(data_frame_logic_new.generate_df_age_in_years_num_patient_dimension()), int)

    def test_generate_df_race_cd_patient_dimension(self):
        from backend.data_frame_logic import data_frame_logic_new

        self.assertEqual(len(data_frame_logic_new.generate_df_race_cd_patient_dimension()), 134)
        self.assertIsInstance(len(data_frame_logic_new.generate_df_race_cd_patient_dimension()), int)

    def test_generate_df_income_cd_patient_dimension(self):
        from backend.data_frame_logic import data_frame_logic_new

        self.assertEqual(len(data_frame_logic_new.generate_df_income_cd_patient_dimension()), 134)
        self.assertIsInstance(len(data_frame_logic_new.generate_df_income_cd_patient_dimension()), int)

    def test_generate_df_only_pat_num(self):
        from backend.data_frame_logic import data_frame_logic_new

        self.assertEqual(len(data_frame_logic_new.generate_df_only_pat_num()), 6455)
        self.assertIsInstance(len(data_frame_logic_new.generate_df_only_pat_num()), int)
