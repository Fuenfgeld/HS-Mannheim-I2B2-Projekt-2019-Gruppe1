import unittest
from backend.abfragenLogik import gesamt_anzahl as sg


class TestSqlGesamtanzahl(unittest.TestCase):

    def test_gesamtanzahlPatienten(self):
        self.assertIsInstance(sg.gesamtanzahlPatienten(), int)
        self.assertGreater(sg.gesamtanzahlPatienten(), -1)
        self.assertEqual(sg.gesamtanzahlPatienten(), 134)

    def test_gesamtanzahlGeschlecht(self):
        self.assertIsInstance(sg.gesamtanzahlGeschlecht('M'), int)
        self.assertGreater(sg.gesamtanzahlGeschlecht('M'), -1)
        self.assertEqual(sg.gesamtanzahlGeschlecht('F'), 52)
        self.assertEqual(sg.gesamtanzahlGeschlecht('L'), 0)

    def test_gesamtanzahlEthnie(self):
        self.assertIsInstance(sg.gesamtanzahlEthnie('black'), int)
        self.assertEqual(sg.gesamtanzahlEthnie('test'), 0)
        i = sg.gesamtanzahlEthnie('black') + sg.gesamtanzahlEthnie('white') + \
            sg.gesamtanzahlEthnie('asian') + sg.gesamtanzahlEthnie('indian') + \
            sg.gesamtanzahlEthnie('hispanic')
        self.assertGreater(i, -1)


    def test_gesamtanzahlFamilienstatus(self):
        self.assertIsInstance(sg.gesamtanzahlFamilienstatus('single'), int)
        self.assertEqual(sg.gesamtanzahlFamilienstatus('test'), 0)
        i = sg.gesamtanzahlFamilienstatus('single') + sg.gesamtanzahlFamilienstatus('married') + \
            sg.gesamtanzahlFamilienstatus('widow') + sg.gesamtanzahlFamilienstatus('divorced')
        self.assertGreater(i, -1)


