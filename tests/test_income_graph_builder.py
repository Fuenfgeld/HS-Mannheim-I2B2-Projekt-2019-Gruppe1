import unittest


class testIncomeGraphBuilder(unittest.TestCase):

    def test_build_income_graph(self):
        import backend.graph_logic.income_graph_builder as igb
        from deprecated import query_bar_logic
        queryBarObject = query_bar_logic.queryBar()

        self.assertIsInstance(igb.build_income_graph(queryBarObject), dict)