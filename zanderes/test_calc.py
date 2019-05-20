import unittest
from zanderes import calc as c


class TestCalc(unittest.TestCase): #unittest.TestCase muss übergeben werden

    def test_add(self): #muss mit test_ anfangen! Dann Name der zu testenden Methode
        self.assertEqual(c.add(10,5), 15)
        self.assertEqual(c.add(-1, 1), 0)
        self.assertEqual(c.add(-1, -1), -2)