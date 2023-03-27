import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(400)
        self.vajaakortti = Maksukortti(100)

    def test_kassan_alustettu_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_alustettu_edulliset_lounaat_lkm_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassan_alustettu_maukkaat_lounaat_lkm_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukas_kateisosto_riittava_maksu_lkm_muuttuu(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_kateisosto_riittava_maksu_lkm_muuttuu(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_kateisosto_riittava_maksu_kassassa_rahaa_muuttuu(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_edullinen_kateisosto_riittava_maksu_kassassa_rahaa_muuttuu(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_maukas_kateisosto_oikea_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(vaihtoraha, 50)

    def test_edullinen_kateisosto_oikea_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(vaihtoraha, 10)

    def test_edullinen_kateisosto_vajaa_summma_lkm_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_kateisosto_vajaa_summma_lkm_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kateisosto_vajaa_summma_kassa_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_kateisosto_vajaa_summma_kassa_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_kateisosto_vajaa_oikea_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(vaihtoraha, 390)

    def test_edullinen_kateisosto_vajaa_oikea_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(vaihtoraha, 230)

    def test_korttimaksu_onnistuu_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)

    def test_korttimaksu_onnistuu_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)

    def test_korttismaksu_onnistuu_edullisesti_lkm_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttismaksu_onnistuu_maukkaasti_lkm_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttimaksu_ei_onnistu_edullisesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.vajaakortti), False)

    def test_korttimaksu_ei_onnistu_maukkaasti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.vajaakortti), False)

    def test_korttismaksu_ei_onnistu_edullisesti_lkm_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.vajaakortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttismaksu_ei_onnistu_maukkaasti_lkm_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.vajaakortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttimaksu_edullinen_kassassa_rahaa_muuttumaton(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_korttimaksu_maukkaasti_kassassa_rahaa_muuttumaton(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 200)
        self.assertEqual(self.kortti.saldo, 600)

    def test_lataa_rahaa_kortille_kassan_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)

    def test_lataa_negatiivinen_summa_kortille_kortin_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -10)
        self.assertEqual(self.kortti.saldo, 400)