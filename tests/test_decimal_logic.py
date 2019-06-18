import unittest


class testDecimalBuilder(unittest.TestCase):

    def test_build_decimal(self):
        import backend.graph_logic.decimal_logic as dl
        from backend.query_bar_logic import query_bar_logic
        import dash_html_components as html
        queryBarObject = query_bar_logic.queryBar()

        self.assertIsInstance(dl.build_decimal(queryBarObject), (html.H5))