import unittest

testmodules = ['test_data_frame_logic', 'test_query_bar_logic', 'test_result_merge',
               'test_sql_builder', 'test_DB_queries']

suite = unittest.TestSuite()

for t in testmodules:
    try:
        mod = __import__(t, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn)
    except(ImportError, AttributeError):
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner(verbosity=2).run(suite)