import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.maksukortti= Maksukortti(1000)
        self.kassapaate= Kassapaate()

    def test_rahamäärä_ja_myydyt_lounaat_alussa_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_käteisosto_toimii_edulliset_kanssa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_liian_pieni_käteisosto_edulliset_ei_muuta_tilannetta(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_käteisosto_toimii_maukkaiden_kanssa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_liian_pieni_käteisosto_maukkaat_ei_muuta_tilannetta(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_korttiosto_toimii_kun_tarpeeksi_rahaa_edulliset(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")
        self.assertEqual(self.kassapaate.edulliset, 1)


    def test_korttiosto_toimii_kun_ei_tarpeeksi_rahaa_edulliset(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")
        self.assertEqual(self.kassapaate.edulliset, 0)


    def test_korttiosto_toimii_kun_tarpeeksi_rahaa_maukkaat(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_korttiosto_toimii_kun_ei_tarpeeksi_rahaa_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")
        self.assertEqual(self.kassapaate.maukkaat, 2)
    
    def test_kassan_määrä_ei_muutu_kortilla_ostaessa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_lataa_rahaa_kortille_kasvattaa_kortin_saldoa_ja_kassan_rahamäärää(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)
        self.assertEqual(str(self.maksukortti), "saldo: 12.0")

    def test_lataa_negatiivinen_summa_kortille_ei_onnistu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")    
