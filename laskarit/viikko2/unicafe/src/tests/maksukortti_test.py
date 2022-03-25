import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_rahan_lataus_onnistuu(self):
        self.maksukortti.lataa_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.15")
    
    
    def test_rahan_ottaminen_vähentää_saldoa_oikein(self):
        #self.maksukortti.ota_rahaa(5)
        self.assertTrue(self.maksukortti.ota_rahaa(5))
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
    
    def test_rahan_ottaminen_ei_onnistu_jos_saldo_liian_pieni(self):
        self.assertFalse(self.maksukortti.ota_rahaa(15))
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
