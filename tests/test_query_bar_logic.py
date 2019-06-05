import unittest


class testQueryBar(unittest.TestCase):

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