import unittest


class testBesidesDiagnosesGraphBuilder(unittest.TestCase):

    def test_build_besides_diagnoses_graph(self):
        import backend.graph_logic.besides_diagnoses_graph_builder as bdgb
        from backend.query_bar_logic import query_bar_logic_new
        from backend.result_logic import result_merge
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()
        resultMergeObject = result_merge.resultMerge()

        self.assertIsInstance(bdgb.build_besides_diagnoses_graph(queryBarLogicObject, resultMergeObject), dict)