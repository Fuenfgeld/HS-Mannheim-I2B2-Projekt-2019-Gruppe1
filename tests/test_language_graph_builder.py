import unittest


class testLanguageGraphBuilder(unittest.TestCase):

    def test_build_language_graph(self):
        import backend.graph_logic.language_graph_builder as lgb
        from backend.query_bar_logic import query_bar_logic_new
        from backend.result_logic import result_merge
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()
        resultMergeObject = result_merge.resultMerge()

        self.assertIsInstance(lgb.build_language_graph(queryBarLogicObject, resultMergeObject), dict)