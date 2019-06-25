import unittest


class testQueryBar(unittest.TestCase):

    def test_append_selection(self):
        from backend.query_bar_logic import query_bar_logic_new
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()

        name = 'Lumbago'
        queryBarLogicObject.append_selection(name)
        self.assertIsInstance(queryBarLogicObject.name_list[0], str)
        self.assertEqual(queryBarLogicObject.name_list[0], 'Lumbago')
        self.assertEqual(len(queryBarLogicObject.df_list[0]), 20)
        self.assertEqual(len(queryBarLogicObject.current_over_all_df), 20)

    def test_delete_all(self):
        from backend.query_bar_logic import query_bar_logic_new
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()

        name = 'Lumbago'
        queryBarLogicObject.append_selection(name)
        queryBarLogicObject.delete_all()
        self.assertIsNot(queryBarLogicObject.name_list, list)
        self.assertIsNot(queryBarLogicObject.df_list, list)
        self.assertEqual(len(queryBarLogicObject.current_over_all_df), 134)
        self.assertEqual(queryBarLogicObject.con_list[0], 'AND')
        self.assertEqual(queryBarLogicObject.con_list[1], 'AND')

    def test_get_actual_over_all_df(self):
        from backend.query_bar_logic import query_bar_logic_new
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()

        self.assertEqual(len(queryBarLogicObject.get_actual_over_all_df()), 134)

    def test_update_current_over_all_df(self):
        from backend.query_bar_logic import query_bar_logic_new
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()

        self.assertEqual(len(queryBarLogicObject.get_actual_over_all_df()), 134)

    def test_append_name_list(self):
        from backend.query_bar_logic import query_bar_logic_new
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()

        queryBarLogicObject.append_name_list('Lumbago')
        self.assertEqual(queryBarLogicObject.name_list[0], 'Lumbago')

    def test_delete_name_list_items(self):
        from backend.query_bar_logic import query_bar_logic_new
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()

        queryBarLogicObject.append_name_list('Lumbago')
        queryBarLogicObject.delete_name_list_items()
        self.assertIsNot(queryBarLogicObject.name_list, list)

    def test_append_df_list(self):
        from backend.query_bar_logic import query_bar_logic_new
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()

        queryBarLogicObject.append_selection('Lumbago')
        self.assertEqual(len(queryBarLogicObject.df_list[0]), 20)

    def test_delete_df_list(self):
        from backend.query_bar_logic import query_bar_logic_new
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()

        queryBarLogicObject.append_selection('Lumbago')
        queryBarLogicObject.delete_df_list()
        self.assertIsNot(queryBarLogicObject.df_list, list)


