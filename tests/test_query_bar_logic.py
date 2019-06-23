import unittest


class testQueryBar(unittest.TestCase):

    def test_get_icd_code_from_name(self):
        from deprecated import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        name = 'Lumbago'
        self.assertIsInstance(queryBarLogicObject.get_icd_code_from_name(name), str)
        self.assertEqual(queryBarLogicObject.get_icd_code_from_name(name), 'select distinct c_basecode from '
                                                                           'i2b2metadata.i2b2 where c_name = \'Lumbago\'')

    def test_append_icd_list(self):
        from deprecated import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        code = 'Lumbago'
        queryBarLogicObject.append_icd_list(queryBarLogicObject, code)
        self.assertIsInstance(queryBarLogicObject.icd_list[0], str)
        self.assertEqual(queryBarLogicObject.icd_list[0], 'ICD9:724.2')
        code1 = 'Bronchiectasis'
        queryBarLogicObject.append_icd_list(queryBarLogicObject, code1)
        self.assertEqual(queryBarLogicObject.icd_list[0], 'ICD9:724.2')
        self.assertEqual(queryBarLogicObject.icd_list[1], 'ICD9:494')


    def test_delete_list_items(self):
        from deprecated import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.delete_icd_list_items()
        self.assertIsInstance(queryBarLogicObject.icd_list, list)
        self.assertEqual(len(queryBarLogicObject.icd_list), 0)


    def test_append_name_list(self):
        from deprecated import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        name = 'Lumbago'
        queryBarLogicObject.append_name_list(name)
        self.assertIsInstance(queryBarLogicObject.name_list, list)
        self.assertIsInstance(queryBarLogicObject.name_list[0], str)
        name1 = 'Bronchitis'
        queryBarLogicObject.append_name_list(name1)
        self.assertEqual(queryBarLogicObject.name_list[1], ' AND ')
        self.assertEqual(queryBarLogicObject.name_list[2], 'Bronchitis')


    def test_delete_name_list_items(self):
        from deprecated import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.delete_name_list_items()
        self.assertIsInstance(queryBarLogicObject.name_list, list)
        self.assertEqual(len(queryBarLogicObject.name_list), 0)


    # vorläufig
    def test_get_all_patients_within_icd_list(self):
        from deprecated import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.get_all_patients_within_icd_list()
        self.assertIsInstance((queryBarLogicObject.name_list), list)


    def test_get_all_patients_within_icd_list_1(self):
        from deprecated import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.icd_list.append('ICD9:724.2')
        queryBarLogicObject.get_all_patients_within_icd_list()
        self.assertIsInstance((queryBarLogicObject.name_list), list)

    def test_get_all_patients_within_icd_list_2(self):
        from deprecated import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.icd_list.append('ICD9:724.2')
        queryBarLogicObject.name_list.append('Lumbago')
        queryBarLogicObject.name_list.append('AND')
        queryBarLogicObject.icd_list.append('ICD9:494')
        queryBarLogicObject.name_list.append('Bronchiectasis')
        queryBarLogicObject.name_list.append('AND')
        queryBarLogicObject.get_all_patients_within_icd_list()
        self.assertIsInstance((queryBarLogicObject.name_list), list)

    def test_get_all_patients_within_icd_list_3(self):
        from deprecated import query_bar_logic
        queryBarLogicObject = query_bar_logic.queryBar()

        queryBarLogicObject.icd_list.append('ICD9:724.2')
        queryBarLogicObject.name_list.append('Lumbago')
        queryBarLogicObject.icd_list.append('ICD9:494')
        queryBarLogicObject.name_list.append('Bronchiectasis')
        queryBarLogicObject.name_list.append('AND')
        queryBarLogicObject.icd_list.append('ICD9:462')
        queryBarLogicObject.name_list.append('Pharyngitis')
        queryBarLogicObject.name_list.append('AND')
        queryBarLogicObject.get_all_patients_within_icd_list()
        self.assertIsInstance((queryBarLogicObject.name_list), list)



