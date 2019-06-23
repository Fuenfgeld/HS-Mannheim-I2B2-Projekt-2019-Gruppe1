import unittest


class testRaceGraphBuilder(unittest.TestCase):

    def test_build_race_graph(self):
        import backend.graph_logic.race_graph_builder as rgb
        from deprecated import query_bar_logic
        queryBarObject = query_bar_logic.queryBar()

        self.assertIsInstance(rgb.build_race_graph(queryBarObject), dict)