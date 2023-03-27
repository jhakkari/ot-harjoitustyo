import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(400)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 14.00 euroa")

    def test_ota_rahaa_vahentaa_saldoa_jos_katetta(self):
        self.assertTrue(self.maksukortti.ota_rahaa(20))

    def test_ota_rahaa_ei_vahenna_saldoa_ei_katetta(self):
        self.assertFalse(self.maksukortti.ota_rahaa(12000))