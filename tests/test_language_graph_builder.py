import unittest


class testLanguageGraphBuilder(unittest.TestCase):

    def test_build_language_graph(self):
        import backend.graph_logic.language_graph_builder as lgb
        from deprecated import query_bar_logic
        queryBarObject = query_bar_logic.queryBar()

        self.assertIsInstance(lgb.build_language_graph(queryBarObject), dict)