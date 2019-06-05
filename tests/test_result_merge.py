import unittest


class testResultMerge(unittest.TestCase):


    def test_merge_two_df(self):
        import pandas
        from config import database
        import backend.result_logic.result_merge as rm
        df = pandas.read_sql('select patient_num from i2b2demodata.patient_dimension', con=database.engine)

        self.assertEqual(len(rm.merge_two_df(df, 'sex_cd')), 134)
        self.assertEqual(len(rm.merge_two_df(df, 'language_cd')), 134)
        self.assertEqual(len(rm.merge_two_df(df, 'age_in_years_num')), 134)