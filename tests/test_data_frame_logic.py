import unittest

class backend_def_test(unittest.TestCase):

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

    def test_merge_two_df(self):
        import pandas
        from config import database
        import backend.result_logic.result_merge as rm
        df = pandas.read_sql('select patient_num from i2b2demodata.patient_dimension', con=database.engine)

        self.assertEqual(len(rm.merge_two_df(df, 'sex_cd')), 134)
        self.assertEqual(len(rm.merge_two_df(df, 'language_cd')), 134)
        self.assertEqual(len(rm.merge_two_df(df, 'age_in_years_num')), 134)

    def test_build_sql_i2b2_patient_dimension_patient_num(self):
        import pandas
        from config import database
        import backend.sql_logic.sql_builder as sqlb

        self.assertIsInstance(sqlb.build_SQL_i2b2_patient_dimension_patient_num(), str)
        self.assertTrue(sqlb.build_SQL_i2b2_patient_dimension_patient_num(),
                        'select sex_cd, patient_num from i2b2demodata.patient_dimension')

    def test_build_SQL_i2b2_observation_fact_1_criterium(self):
        import backend.sql_logic.sql_builder as sqlb

        self.assertIsInstance(sqlb.build_SQL_i2b2_observation_fact_1_criterium('ICD9:724.2'), str)

    def test_build_SQL_i2b2_observation_fact_2_criteria(self):
        import backend.sql_logic.sql_builder as sqlb

        self.assertIsInstance(sqlb.build_SQL_i2b2_observation_fact_2_criteria('ICD9:724.2', 'ICD9:724.2'), str)

    def test_build_SQL_i2b2_metadata_i2b2_code(self):
        import backend.sql_logic.sql_builder as sqlb

        self.assertIsInstance(sqlb.build_SQL_i2b2_metadata_i2b2_code('Lumbago'), str)

    def test_build_SQL_i2b2_oservation_fact_1_criterium_name(self):
        import backend.sql_logic.sql_builder as sqlb

        self.assertIsInstance(sqlb.build_SQL_i2b2_oservation_fact_1_criterium_name('ICD9:724.2'), str)

    def test_build_SQL_i2b2_oservation_fact_2_criteria_name(self):
        import backend.sql_logic.sql_builder as sqlb

        self.assertIsInstance(sqlb.build_SQL_i2b2_oservation_fact_2_criteria_name('ICD9:724.2', 'ICD9:724.2'), str)

    def test_get_icd_code_from_name(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        name = 'Lumbago'
        self.assertIsInstance(queryBarLogicObject.get_icd_code_from_name(name), str)
        self.assertEqual(queryBarLogicObject.get_icd_code_from_name(name), 'select distinct c_basecode from '
                                                                           'i2b2metadata.i2b2 where c_name = \'Lumbago\'')

    def test_append_list_decimal(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        code = 'ICD9'
        queryBarLogicObject.append_icd_list_decimal(code)
        self.assertIsInstance(queryBarLogicObject.icd_list_decimal[0], str)
        self.assertEqual(queryBarLogicObject.icd_list_decimal[0], 'ICD9')
        code1 = 'ICD9:1'
        queryBarLogicObject.append_icd_list_decimal(code1)
        self.assertEqual(queryBarLogicObject.icd_list_decimal[0], 'ICD9')
        self.assertEqual(queryBarLogicObject.icd_list_decimal[1], 'ICD9:1')

    def test_delete_list_decimal_items(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.delete_icd_list_decimal_items()
        self.assertIsInstance(queryBarLogicObject.icd_list_decimal, list)
        self.assertEqual(len(queryBarLogicObject.icd_list_decimal), 0)

    def test_append_list_sex_cd(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        code = 'ICD9'
        queryBarLogicObject.append_icd_list_sex_cd(code)
        self.assertIsInstance(queryBarLogicObject.icd_list_sex_cd[0], str)
        self.assertEqual(queryBarLogicObject.icd_list_sex_cd[0], 'ICD9')
        code1 = 'ICD9:1'
        queryBarLogicObject.append_icd_list_sex_cd(code1)
        self.assertEqual(queryBarLogicObject.icd_list_sex_cd[0], 'ICD9')
        self.assertEqual(queryBarLogicObject.icd_list_sex_cd[1], 'ICD9:1')

    def test_delete_list_sex_cd_items(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.delete_icd_list_sex_cd_items()
        self.assertIsInstance(queryBarLogicObject.icd_list_sex_cd, list)
        self.assertEqual(len(queryBarLogicObject.icd_list_sex_cd), 0)

    def test_append_list_language_cd(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        code = 'ICD9'
        queryBarLogicObject.append_icd_list_language_cd(code)
        self.assertIsInstance(queryBarLogicObject.icd_list_language_cd[0], str)
        self.assertEqual(queryBarLogicObject.icd_list_language_cd[0], 'ICD9')
        code1 = 'ICD9:1'
        queryBarLogicObject.append_icd_list_language_cd(code1)
        self.assertEqual(queryBarLogicObject.icd_list_language_cd[0], 'ICD9')
        self.assertEqual(queryBarLogicObject.icd_list_language_cd[1], 'ICD9:1')

    def test_delete_list_language_cd_items(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.delete_icd_list_language_cd_items()
        self.assertIsInstance(queryBarLogicObject.icd_list_language_cd, list)
        self.assertEqual(len(queryBarLogicObject.icd_list_language_cd), 0)

    def test_append_list_age_in_years_num(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        code = 'ICD9'
        queryBarLogicObject.append_icd_list_age_in_years_num(code)
        self.assertIsInstance(queryBarLogicObject.icd_list_age_in_years_num[0], str)
        self.assertEqual(queryBarLogicObject.icd_list_age_in_years_num[0], 'ICD9')
        code1 = 'ICD9:1'
        queryBarLogicObject.append_icd_list_age_in_years_num(code1)
        self.assertEqual(queryBarLogicObject.icd_list_age_in_years_num[0], 'ICD9')
        self.assertEqual(queryBarLogicObject.icd_list_age_in_years_num[1], 'ICD9:1')

    def test_delete_list_age_in_years_num_items(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.delete_icd_list_age_in_years_num_items()
        self.assertIsInstance(queryBarLogicObject.icd_list_age_in_years_num, list)
        self.assertEqual(len(queryBarLogicObject.icd_list_age_in_years_num), 0)

    def test_append_name_list(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        name = 'Lumbago'
        queryBarLogicObject.append_name_list(name)
        self.assertIsInstance(queryBarLogicObject.name_list, list)
        self.assertIsInstance(queryBarLogicObject.name_list[0], str)
        name1 = 'Bronchitis'
        queryBarLogicObject.append_name_list(name1)
        self.assertEqual(queryBarLogicObject.name_list[1], ' AND ')
        self.assertEqual(queryBarLogicObject.name_list[2], 'Bronchitis')

    def test_print_name_list(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject = query_bar_logic.queryBar()
        self.assertNotIsInstance(queryBarLogicObject.print_name_list(), list)
        name = 'Lumbago'
        queryBarLogicObject.append_name_list(name)
        self.assertIsInstance(queryBarLogicObject.name_list, list)
        self.assertEqual(queryBarLogicObject.name_list[0], 'Lumbago')

    def test_delete_name_list_items(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.delete_name_list_items()
        self.assertIsInstance(queryBarLogicObject.name_list, list)
        self.assertEqual(len(queryBarLogicObject.name_list), 0)

    # vorläufig
    def test_get_all_patients_within_icd_list_decimal(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.get_all_patients_within_icd_list_decimal()
        self.assertIsInstance((queryBarLogicObject.name_list), list)

    def test_get_all_patients_within_icd_list_decimal1(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.icd_list_decimal.append('ICD9:724.2')
        queryBarLogicObject.get_all_patients_within_icd_list_decimal()
        self.assertIsInstance((queryBarLogicObject.name_list), list)

    def test_get_all_patients_within_icd_list_decimal2(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.icd_list_decimal.append('ICD9:724.2')
        queryBarLogicObject.get_all_patients_within_icd_list_decimal()
        self.assertIsInstance((queryBarLogicObject.name_list), list)

    def test_get_all_patients_within_icd_list_sex_cd(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.get_all_patients_within_icd_list_sex_cd()
        self.assertIsInstance((queryBarLogicObject.name_list), list)

    def test_get_all_patients_within_icd_list_sex_cd1(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.icd_list_sex_cd.append('ICD9:724.2')
        queryBarLogicObject.get_all_patients_within_icd_list_sex_cd()
        self.assertIsInstance((queryBarLogicObject.name_list), list)

    def test_get_all_patients_within_icd_list_sex_cd2(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.icd_list_sex_cd.append('ICD9:724.2')
        queryBarLogicObject.get_all_patients_within_icd_list_sex_cd()
        self.assertIsInstance((queryBarLogicObject.name_list), list)

    def test_get_all_patients_within_icd_list_language_cd(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.get_all_patients_within_icd_list_language_cd()
        self.assertIsInstance((queryBarLogicObject.name_list), list)

    def test_get_all_patients_within_icd_list_language_cd1(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.icd_list_language_cd.append('ICD9:724.2')
        queryBarLogicObject.get_all_patients_within_icd_list_language_cd()
        self.assertIsInstance((queryBarLogicObject.name_list), list)

    def test_get_all_patients_within_icd_list_language_cd2(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.icd_list_language_cd.append('ICD9:724.2')
        queryBarLogicObject.get_all_patients_within_icd_list_language_cd()
        self.assertIsInstance((queryBarLogicObject.name_list), list)

    def test_get_all_patients_within_icd_list_age_in_years_num(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.get_all_patients_within_icd_list_age_in_years_num()
        self.assertIsInstance((queryBarLogicObject.name_list), list)

    def test_get_all_patients_within_icd_list_age_in_years_num1(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.icd_list_age_in_years_num.append('ICD9:724.2')
        queryBarLogicObject.get_all_patients_within_icd_list_age_in_years_num()
        self.assertIsInstance((queryBarLogicObject.name_list), list)

    def test_get_all_patients_within_icd_list_age_in_years_num2(self):
        from backend.query_bar_logic import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.icd_list_age_in_years_num.append('ICD9:724.2')
        queryBarLogicObject.get_all_patients_within_icd_list_age_in_years_num()
        self.assertIsInstance((queryBarLogicObject.name_list), list)