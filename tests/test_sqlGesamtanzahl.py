import unittest
from abfragenLogik import sqlGesamtanzahl as sg

class TestSqlGesamtanzahl(unittest.TestCase):

    def test_gesamtanzahlPatienten(self):
        self.assertIsInstance(sg.gesamtanzahlPatienten(), int)
        self.assertGreater(sg.gesamtanzahlPatienten(), 0)
        self.assertEqual(sg.gesamtanzahlPatienten(), 134)

    def test_gesamtanzahlGeschlecht(self):
        self.assertEqual(sg.gesamtanzahlGeschlecht('M'), 82)
