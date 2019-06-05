import unittest

import pandas.io.sql as psql

from backend.tree_logic import DB_queries as db


class MyTestCase(unittest.TestCase):

    def test_get_level_first_level(self):
        testQuery = db.Queries()
        methodDataFrame = db.Queries.get_level(testQuery, )
        testDataFrame = psql.read_sql(
            "select c_name as name, c_path as path, c_basecode as icdcode, c_hlevel as level, c_fullname as fullname "
            f"from i2b2metadata.icd10_icd9 where c_hlevel = 1 and c_basecode like 'ICD%' "
            f"order by c_hlevel, c_fullname ",
            con=testQuery.connection)

        methodDataFrame == testDataFrame

    def test_get_level_second_level(self):
        testQuery = db.Queries()
        methodDataFrame = db.Queries.get_level(testQuery, 2)
        testDataFrame = psql.read_sql(
            "select c_name as name, c_path as path, c_basecode as icdcode, c_hlevel as level, c_fullname as fullname "
            f"from i2b2metadata.icd10_icd9 where c_hlevel = 2 and c_basecode like 'ICD%' "
            f"order by c_hlevel, c_fullname ",
            con=testQuery.connection)

        methodDataFrame == testDataFrame

    def test_get_level_third_level(self):
        testQuery = db.Queries()
        methodDataFrame = db.Queries.get_level(testQuery, 3)
        testDataFrame = psql.read_sql(
            "select c_name as name, c_path as path, c_basecode as icdcode, c_hlevel as level, c_fullname as fullname "
            f"from i2b2metadata.icd10_icd9 where c_hlevel = 3 and c_basecode like 'ICD%' "
            f"order by c_hlevel, c_fullname ",
            con=testQuery.connection)

        methodDataFrame == testDataFrame

    def test_get_level_fourth_level(self):
        testQuery = db.Queries()
        methodDataFrame = db.Queries.get_level(testQuery, 4)
        testDataFrame = psql.read_sql(
            "select c_name as name, c_path as path, c_basecode as icdcode, c_hlevel as level, c_fullname as fullname "
            f"from i2b2metadata.icd10_icd9 where c_hlevel = 4 and c_basecode like 'ICD%' "
            f"order by c_hlevel, c_fullname ",
            con=testQuery.connection)

        methodDataFrame == testDataFrame

    def test_get_level_fifth_level(self):
        testQuery = db.Queries()
        methodDataFrame = db.Queries.get_level(testQuery, 5)
        testDataFrame = psql.read_sql(
            "select c_name as name, c_path as path, c_basecode as icdcode, c_hlevel as level, c_fullname as fullname "
            f"from i2b2metadata.icd10_icd9 where c_hlevel = 5 and c_basecode like 'ICD%' "
            f"order by c_hlevel, c_fullname ",
            con=testQuery.connection)

        methodDataFrame == testDataFrame

    def test_get_level_sixth_level(self):
        testQuery = db.Queries()
        methodDataFrame = db.Queries.get_level(testQuery, 6)
        testDataFrame = psql.read_sql(
            "select c_name as name, c_path as path, c_basecode as icdcode, c_hlevel as level, c_fullname as fullname "
            f"from i2b2metadata.icd10_icd9 where c_hlevel = 6 and c_basecode like 'ICD%' "
            f"order by c_hlevel, c_fullname ",
            con=testQuery.connection)

        methodDataFrame == testDataFrame

    def test_get_level_seventh_level(self):
        testQuery = db.Queries()
        methodDataFrame = db.Queries.get_level(testQuery, 7)
        testDataFrame = psql.read_sql(
            "select c_name as name, c_path as path, c_basecode as icdcode, c_hlevel as level, c_fullname as fullname "
            f"from i2b2metadata.icd10_icd9 where c_hlevel = 7 and c_basecode like 'ICD%' "
            f"order by c_hlevel, c_fullname ",
            con=testQuery.connection)

        methodDataFrame == testDataFrame

    def test_get_level_eighth_level(self):
        testQuery = db.Queries()
        methodDataFrame = db.Queries.get_level(testQuery, 8)
        testDataFrame = psql.read_sql(
            "select c_name as name, c_path as path, c_basecode as icdcode, c_hlevel as level, c_fullname as fullname "
            f"from i2b2metadata.icd10_icd9 where c_hlevel = 8 and c_basecode like 'ICD%' "
            f"order by c_hlevel, c_fullname ",
            con=testQuery.connection)

        methodDataFrame == testDataFrame

    def test_get_level_ninth_level(self):
        testQuery = db.Queries()
        methodDataFrame = db.Queries.get_level(testQuery, 9)
        testDataFrame = psql.read_sql(
            "select c_name as name, c_path as path, c_basecode as icdcode, c_hlevel as level, c_fullname as fullname "
            f"from i2b2metadata.icd10_icd9 where c_hlevel = 9 and c_basecode like 'ICD%' "
            f"order by c_hlevel, c_fullname ",
            con=testQuery.connection)

        methodDataFrame == testDataFrame

    def test_get_level_tenth_level(self):
        testQuery = db.Queries()
        methodDataFrame = db.Queries.get_level(testQuery, 10)
        testDataFrame = psql.read_sql(
            "select c_name as name, c_path as path, c_basecode as icdcode, c_hlevel as level, c_fullname as fullname "
            f"from i2b2metadata.icd10_icd9 where c_hlevel = 10 and c_basecode like 'ICD%' "
            f"order by c_hlevel, c_fullname ",
            con=testQuery.connection)

        methodDataFrame == testDataFrame


if __name__ == '__main__':
    unittest.main()
