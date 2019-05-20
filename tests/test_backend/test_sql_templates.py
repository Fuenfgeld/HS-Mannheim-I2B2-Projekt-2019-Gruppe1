import unittest
from backend.abfragenLogik import sql_templates as sql_templates

sqlTemplates = sql_templates.SQLTemplates()

class TestSQLTemplates(unittest.TestCase):

    def test_pat_df_ein_kriterium_i2b2(self):
        self.assertEqual(len(sqlTemplates.c_basecode_from_i2b2_ein_kriterium_blatt("Hypertensive renal disease")), 1)
        self.assertIsInstance(len(sqlTemplates.c_basecode_from_i2b2_ein_kriterium_blatt("Hypertensive renal disease")), int)

