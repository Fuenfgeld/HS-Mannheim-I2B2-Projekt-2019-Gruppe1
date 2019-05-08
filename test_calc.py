import unittest
import calc as c #zu testende files importen

class TestCalc(unittest.TestCase): #unittest.TestCase muss übergeben werden

    def test_add(self): #muss mit test_ anfangen! Dann Name der zu testenden Methode
        result = c.add(10,5)
        self.assertEqual(result, 15)
