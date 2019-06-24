import unittest


class testSexGraphBuilder(unittest.TestCase):

    def test_build_sex_graph(self):
        import backend.graph_logic.sex_graph_builder as sgb
        from backend.query_bar_logic import query_bar_logic_new
        from backend.result_logic import result_merge
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()
        resultMergeObject = result_merge.resultMerge()

        self.assertIsInstance(sgb.build_sex_graph(queryBarLogicObject, resultMergeObject), dict)