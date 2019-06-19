import unittest


class testAgeGraphBuilder(unittest.TestCase):

    def test_build_age_graph(self):
        import backend.graph_logic.age_graph_builder as agb
        from backend.query_bar_logic import query_bar_logic
        queryBarObject = query_bar_logic.queryBar()

        self.assertIsInstance(agb.build_age_graph(queryBarObject), dict)