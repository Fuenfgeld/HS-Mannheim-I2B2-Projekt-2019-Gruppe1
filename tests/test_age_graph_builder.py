import unittest


class testAgeGraphBuilder(unittest.TestCase):

    def test_build_age_graph(self):
        import backend.graph_logic.age_graph_builder as agb
        from backend.query_bar_logic import query_bar_logic_new
        from backend.result_logic import result_merge
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()
        resultMergeObject = result_merge.resultMerge()

        self.assertIsInstance(agb.build_age_graph(queryBarLogicObject, resultMergeObject), dict)