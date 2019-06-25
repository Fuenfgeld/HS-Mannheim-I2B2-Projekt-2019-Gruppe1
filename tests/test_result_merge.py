import unittest


class testResultMerge(unittest.TestCase):

    def test_merge_two_df(self):
        import backend.result_logic.result_merge as rm
        from config import database
        import pandas as pd
        df = pd.read_sql(
            f'select sex_cd, language_cd, age_in_years_num, patient_num from i2b2demodata.patient_dimension',
            con=database.engine)
        resultMergeObject = rm.resultMerge()

        self.assertEqual(len(resultMergeObject.merge_two_df(df, 'sex_cd')), 134)
        self.assertEqual(len(resultMergeObject.merge_two_df(df, 'language_cd')), 134)
        self.assertEqual(len(resultMergeObject.merge_two_df(df, 'age_in_years_num')), 134)
