import unittest


class testDecimalBuilder(unittest.TestCase):

    def test_build_decimal(self):
        import backend.graph_logic.decimal_logic as dl
        from backend.query_bar_logic import query_bar_logic_new
        from backend.result_logic import result_merge
        import dash_html_components as html
        queryBarLogicObject = query_bar_logic_new.queryBarLogicNew()
        resultMergeObject = result_merge.resultMerge()

        self.assertIsInstance(dl.build_decimal(queryBarLogicObject, resultMergeObject), (html.H5))