# envelope performance simple unit test
import unittest
import nbimporter

from EnvelopePerformanceSimple import simpleEnvPerformanceSelected as SEPS

class TestSEPS(unittest.TestCase):
    
    def test_gen_includingQdashMhMc(self):
        
        test_patterns = [
                ( '1', 120.08, 29.81, 51.34, '1', '1', 7.7, 6.67, 5.27, 5.27, 4.65, 6.51, 0.7, 0.7, '1', 0.93, 0.51, 1.8, 1.8, 1.8, 6.14, 13.9, 14.7),
                ( '6', 120.08, 29.81, 51.34, '1', '1', 7.7, 6.67, 5.27, 5.27, 4.65, 6.51, 0.7, 0.7, '1', 0.93, 0.51, 1.8, 1.8, 1.8, 6.14, 13.5, 14.4)
                ]
        for region, area_total, area_main, area_other, house_type, bath_ins_type, U_roof, U_wall, U_floorOther, U_floorBath, U_door, U_window, eta_d_cooling, eta_d_heating, fValue_useDefault, fValue_cooling, fValue_heating, psi_perimeterOther, psi_perimeterEntrance, psi_perimeterBath, expected_UA, expected_etaAC, expected_etaAH in test_patterns:
            with self.subTest():
                spec = {
                        'region' : { '1':'region1', '2':'region2', '3':'region3', '4':'region4', '5':'region5', '6':'region6', '7':'region7', '8':'region8' }[region],
                        'house_type' : { '1' : 'floor_ins', '2' : 'base_ins', '3' : 'floor_and_base_ins' }[house_type],
                        'bath_ins_type' : { '1' : 'bath_floor_ins', '2' : 'bath_base_ins', '3' : 'bath_2nd_floor' }[bath_ins_type],
                        'U' : {
                                'roof'         : U_roof,
                                'wall'         : U_wall,
                                'floorOther'   : U_floorOther,
                                'floorBath'    : U_floorBath,
                                'door'         : U_door,
                                'window'       : U_window,
                                },
                        'psi' : {
                                'useDefaultEtrc' : 'no',
                                'prmOther'       : psi_perimeterOther,
                                'prmEtrc'        : psi_perimeterEntrance,
                                'prmBath'        : psi_perimeterBath,
                                },
                        'eta_d' : {
                                'heating' : eta_d_heating,
                                'cooling' : eta_d_cooling
                                },
                        'fValue' : {
                                'useDefault' : { '1' : 'yes', '2' : 'no' }[fValue_useDefault],
                                'heating'    : fValue_heating,
                                'cooling'    : fValue_cooling
                                }
                        }
                actual_UA    = SEPS(spec)['UA']
                actual_etaAH = SEPS(spec)['etaAH']
                actual_etaAC = SEPS(spec)['etaAC']
                self.assertAlmostEqual(actual_UA,    expected_UA,    delta = 0.000001)
                self.assertAlmostEqual(actual_etaAH, expected_etaAH, delta = 0.000001)
                self.assertAlmostEqual(actual_etaAC, expected_etaAC, delta = 0.000001)


if __name__ == "__main__":
    unittest.main()
    