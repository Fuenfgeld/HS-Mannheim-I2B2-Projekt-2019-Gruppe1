import unittest
from SQL.selects.gesamt_anzahl import gesamtAnzahl

gesamt_anzahl = gesamtAnzahl()

class TestStringMethods(unittest.TestCase):

    #gesamt_anzahl
    def test_gesamtanzahlPatienten(self):
        self.assertEqual(gesamt_anzahl.gesamtanzahlPatienten(), 134)


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())