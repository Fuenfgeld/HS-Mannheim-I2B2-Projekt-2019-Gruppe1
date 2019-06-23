import unittest


class testSQLBuilder(unittest.TestCase):

    def test_build_SQL_i2b2_observation_fact_1_criterium(self):
        import deprecated.sql_builder as sqlb

        self.assertIsInstance(sqlb.build_SQL_i2b2_observation_fact_1_criterium('ICD9:724.2'), str)


    def test_build_SQL_i2b2_observation_fact_2_criteria(self):
        import deprecated.sql_builder as sqlb

        self.assertIsInstance(sqlb.build_SQL_i2b2_observation_fact_2_criteria('ICD9:724.2', 'ICD9:724.2', 'AND'), str)


    def test_build_SQL_i2b2_metadata_i2b2_code(self):
        import deprecated.sql_builder as sqlb

        self.assertIsInstance(sqlb.build_SQL_i2b2_metadata_i2b2_code('Lumbago'), str)


    def test_build_SQL_i2b2_oservation_fact_1_criterium_name(self):
        import deprecated.sql_builder as sqlb

        self.assertIsInstance(sqlb.build_SQL_i2b2_oservation_fact_1_criterium_name('ICD9:724.2'), str)


    def test_build_SQL_i2b2_oservation_fact_2_criteria_name(self):
        import deprecated.sql_builder as sqlb

        self.assertIsInstance(sqlb.build_SQL_i2b2_oservation_fact_2_criteria_name('ICD9:724.2', 'ICD9:724.2'), str)