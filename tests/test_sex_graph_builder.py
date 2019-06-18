import unittest


class testSexGraphBuilder(unittest.TestCase):

    def test_build_sex_graph(self):
        import backend.graph_logic.sex_graph_builder as sgb
        from backend.query_bar_logic import query_bar_logic
        queryBarObject = query_bar_logic.queryBar()

        self.assertIsInstance(sgb.build_sex_graph(queryBarObject), dict)