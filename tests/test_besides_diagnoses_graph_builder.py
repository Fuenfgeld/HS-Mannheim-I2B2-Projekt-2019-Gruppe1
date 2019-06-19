import unittest


class testBesidesDiagnosesGraphBuilder(unittest.TestCase):

    def test_build_besides_diagnoses_graph(self):
        import backend.graph_logic.besides_diagnoses_graph_builder as bdgb
        from backend.query_bar_logic import query_bar_logic
        queryBarObject = query_bar_logic.queryBar()

        self.assertIsInstance(bdgb.build_besides_diagnoses_graph(queryBarObject), dict)