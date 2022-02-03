import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
    
    def test_virheellinen_tilavuus_nollautuu(self):
        self.assertAlmostEqual(Varasto(-10).tilavuus, 0)

    def test_virheellinen_alku_saldo_nollautuu(self):
        self.assertAlmostEqual(Varasto(10, -10).saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivinen_lisays_ei_onnistu(self):
        self.varasto.lisaa_varastoon(-8)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_ei_mene_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(20)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_ottaminen_ei_onnistu(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_liika_ottaminen_palauttaa_kaiken(self):
        self.varasto.lisaa_varastoon(8)

        otettu = self.varasto.ota_varastosta(20)

        self.assertAlmostEqual(otettu, 8)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_merkkijono_alussa(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

    def test_merkkijono_lisayksen_jalkeen(self):
        self.varasto.lisaa_varastoon(8)

        self.assertEqual(str(self.varasto), "saldo = 8, vielä tilaa 2")
