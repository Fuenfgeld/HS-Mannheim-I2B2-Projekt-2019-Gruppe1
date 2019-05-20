import unittest
from backend.abfragenLogik import gesamt_anzahl

gesamtAnzahl = gesamt_anzahl.GesamtAnzahl()


class TestGesamtanzahl(unittest.TestCase):

    def test_gesamtanzahlPatienten(self):
        self.assertIsInstance(gesamtAnzahl.gesamtanzahlPatienten(), int)
        self.assertGreater(gesamtAnzahl.gesamtanzahlPatienten(), -1)
        self.assertEqual(gesamtAnzahl.gesamtanzahlPatienten(), 134)

    def test_gesamtanzahlGeschlecht(self):
        self.assertIsInstance(gesamtAnzahl.gesamtanzahlGeschlecht('M'), int)
        self.assertGreater(gesamtAnzahl.gesamtanzahlGeschlecht('M'), -1)
        self.assertEqual(gesamtAnzahl.gesamtanzahlGeschlecht('F'), 52)
        self.assertEqual(gesamtAnzahl.gesamtanzahlGeschlecht('L'), 0)

    def test_gesamtanzahlEthnie(self):
        self.assertIsInstance(gesamtAnzahl.gesamtanzahlEthnie('black'), int)
        self.assertEqual(gesamtAnzahl.gesamtanzahlEthnie('test'), 0)
        i = gesamtAnzahl.gesamtanzahlEthnie('black') + gesamtAnzahl.gesamtanzahlEthnie('white') + \
            gesamtAnzahl.gesamtanzahlEthnie('asian') + gesamtAnzahl.gesamtanzahlEthnie('indian') + \
            gesamtAnzahl.gesamtanzahlEthnie('hispanic')
        self.assertGreater(i, -1)


    def test_gesamtanzahlFamilienstatus(self):
        self.assertIsInstance(gesamtAnzahl.gesamtanzahlFamilienstatus('single'), int)
        self.assertEqual(gesamtAnzahl.gesamtanzahlFamilienstatus('test'), 0)
        i = gesamtAnzahl.gesamtanzahlFamilienstatus('single') + gesamtAnzahl.gesamtanzahlFamilienstatus('married') + \
            gesamtAnzahl.gesamtanzahlFamilienstatus('widow') + gesamtAnzahl.gesamtanzahlFamilienstatus('divorced')
        self.assertGreater(i, -1)


