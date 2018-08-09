# envelope performance simple unit test
import unittest
import nbimporter
import csv

from EnvelopePerformanceSimple import simpleEnvPerformanceSelected as SEPS

class TestSEPS(unittest.TestCase):
    
    def test_gen_includingQdashMhMc(self):
#        f = open('EnvelopePerformanceSimpleTestCase.csv','r',encoding='utf8')
        f = open('test_envelope_simple.txt','r',encoding='shift-JIS')
        #reader = csv.reader(f)
        #header = next(reader.split('\t'))
        header = next(f)
#        for i, row in enumerate(reader):
        for i, row in enumerate(f):
            row = row[:-1].split('\t')
            testcase, region, area_total, area_main, area_other, house_type, bath_ins_type, U_roof, U_wall, U_floorOther, U_floorBath, U_door, U_window, eta_d_cooling, eta_d_heating, fValue_useDefault, fValue_cooling, fValue_heating, psi_perimeterOther, psi_perimeterEntrance, psi_perimeterBath, expected_UA, expected_etaAC, expected_etaAH = tuple(row)
            with self.subTest(testcase):
                spec = {
                        'region' : { '1':'region1', '2':'region2', '3':'region3', '4':'region4', '5':'region5', '6':'region6', '7':'region7', '8':'region8' }[region],
                        'house_type' : { '1' : 'floor_ins', '2' : 'base_ins', '3' : 'floor_and_base_ins' }[house_type],
                        'bath_ins_type' : { '1' : 'bath_floor_ins', '2' : 'bath_base_ins', '3' : 'bath_2nd_floor' }[bath_ins_type],
                        'U' : {
                                'roof'         : float(U_roof),
                                'wall'         : float(U_wall),
                                'floorOther'   : float(U_floorOther),
                                'floorBath'    : float(U_floorBath),
                                'door'         : float(U_door),
                                'window'       : float(U_window),
                                },
                        'psi' : {
                                'useDefaultEtrc' : 'no',
                                'prmOther'       : float(psi_perimeterOther),
                                'prmEtrc'        : float(psi_perimeterEntrance),
                                'prmBath'        : float(psi_perimeterBath),
                                },
                        'eta_d' : {
                                'heating' : float(eta_d_heating),
                                'cooling' : float(eta_d_cooling)
                                },
                        'fValue' : {
                                'useDefault' : { '1' : 'yes', '2' : 'no' }[fValue_useDefault],
                                'heating'    : float(fValue_heating),
                                'cooling'    : float(fValue_cooling)
                                }
                        }
                if 1:
                    #print(spec)
                    #print(SEPS(spec))
                    #print(SEPS(spec)['UA'])
                    #print(expected_UA)
                    #print(SEPS(spec)['etaAH'])
                    #print(expected_etaAH)
                    #print(SEPS(spec)['etaAC'])
                    #print(expected_etaAC)
                    #print(type(SEPS(spec)['UA']))
                    #print(type(expected_UA))
                    actual_UA    = SEPS(spec)['UA']
                    actual_etaAH = SEPS(spec)['etaAH']
                    actual_etaAC = SEPS(spec)['etaAC']
                    self.assertAlmostEqual(actual_UA,    'ND' if expected_UA == 'ND' else float(expected_UA),    delta = 0.000001)
                    self.assertAlmostEqual(actual_etaAH, 'ND' if expected_etaAH == 'ND' else float(expected_etaAH), delta = 0.000001)
                    self.assertAlmostEqual(actual_etaAC, 'ND' if expected_etaAC == 'ND' else float(expected_etaAC), delta = 0.000001)


if __name__ == "__main__":
    unittest.main()
    