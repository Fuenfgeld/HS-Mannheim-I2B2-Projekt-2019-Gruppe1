import unittest


class testRaceGraphBuilder(unittest.TestCase):

    def test_build_race_graph(self):
        import backend.graph_logic.race_graph_builder as rgb
        from backend.query_bar_logic import query_bar_logic_new
        from backend.result_logic import result_merge
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()
        resultMergeObject = result_merge.resultMerge()

        self.assertIsInstance(rgb.build_race_graph(queryBarLogicObject, resultMergeObject), dict)