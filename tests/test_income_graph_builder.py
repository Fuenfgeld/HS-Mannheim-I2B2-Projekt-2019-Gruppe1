import unittest


class testIncomeGraphBuilder(unittest.TestCase):

    def test_build_income_graph(self):
        import backend.graph_logic.income_graph_builder as igb
        from backend.query_bar_logic import query_bar_logic_new
        from backend.result_logic import result_merge
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()
        resultMergeObject = result_merge.resultMerge()

        self.assertIsInstance(igb.build_income_graph(queryBarLogicObject, resultMergeObject), dict)