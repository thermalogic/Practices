# coding=gbk
'''
Created on 2016年3月18日

@author: 1
'''


import unittest
import if97

class FirstExampleTestCase(unittest.TestCase):
    def test_specific_volume(self):
        self.assertEqual(if97.specific_volume(3, 300),0.0010021516796866943)
    def test_specific_enthalpy(self):
        self.assertEqual(if97.specific_enthalpy(3, 300),115.3312730214384)
    def test_specific_internal_energy(self):
        self.assertEqual(if97.specific_internal_energy(3, 300),112.32481798237833)
    def test_specific_entropy(self):
        self.assertEqual(if97.specific_entropy(3, 300),0.39229479240262427)
    def test_specific_isobaric_heat_capacity(self):
        self.assertEqual(if97.specific_isobaric_heat_capacity(3, 300),4.173012184067783)
    def test_speed_of_sound(self):
        self.assertEqual(if97.speed_of_sound(3, 300),1507.7392096690312)
        
class SecondExampleTestCase(unittest.TestCase):
    def test_specific_volume(self):
        self.assertEqual(if97.specific_volume(80, 300),0.0009711808940216297)
    def test_specific_enthalpy(self):
        self.assertEqual(if97.specific_enthalpy(80, 300),184.14282773425438)
    def test_specific_internal_energy(self):
        self.assertEqual(if97.specific_internal_energy(80, 300),106.44835621252402)
    def test_specific_entropy(self):
        self.assertEqual(if97.specific_entropy(80, 300),0.36856385239848066)
    def test_specific_isobaric_heat_capacity(self):
        self.assertEqual(if97.specific_isobaric_heat_capacity(80, 300),4.010089869646331)
    def test_speed_of_sound(self):
        self.assertEqual(if97.speed_of_sound(80, 300),1634.6905431116586)
        
class ThirdExampleTestCase(unittest.TestCase):
    def test_specific_volume(self):
        self.assertEqual(if97.specific_volume(3, 500),0.001202418003378339)
    def test_specific_enthalpy(self):
        self.assertEqual(if97.specific_enthalpy(3, 500),975.5422390972251)
    def test_specific_internal_energy(self):
        self.assertEqual(if97.specific_internal_energy(3, 500),971.9349850870901)
    def test_specific_entropy(self):
        self.assertEqual(if97.specific_entropy(3, 500),2.58041912005181)
    def test_specific_isobaric_heat_capacity(self):
        self.assertEqual(if97.specific_isobaric_heat_capacity(3, 500),4.6558068221112086)
    def test_speed_of_sound(self):
        self.assertEqual(if97.speed_of_sound(3, 500),1240.7133731017252)
        

class FourthExampleTestCase(unittest.TestCase):
    def test_backward_equation_a(self):
        self.assertEqual(if97.backward_equation_a(1700, 3.8), 25.557032462895986)
    def test_backward_equation_b(self):
        self.assertEqual(if97.backward_equation_b(2600, 5.1), 34.34999262770051)

class FifthExampleTestCase(unittest.TestCase):
    def test_backward_equation_a(self):
        self.assertEqual(if97.backward_equation_a(2000, 4.2), 45.40873467774791)
    def test_backward_equation_b(self):
        self.assertEqual(if97.backward_equation_b(2400, 4.7), 63.6392488735417)
        
class SixthExampleTestCase(unittest.TestCase):
    def test_backward_equation_a(self):
        self.assertEqual(if97.backward_equation_a(2100, 4.3), 60.78123340465693)
    def test_backward_equation_b(self):
        self.assertEqual(if97.backward_equation_b(2700, 5.0), 88.39043280879775)
        
def suite_use_make_suite():
    suite = unittest.TestSuite()
    #测试IF97
    suite.addTest(unittest.makeSuite(FirstExampleTestCase))#T=300K,P=3MPa
    suite.addTest(unittest.makeSuite(SecondExampleTestCase))#T=300K,P=80MPa
    suite.addTest(unittest.makeSuite(ThirdExampleTestCase))#T=500K,P=3MPa
    #测试IF97+
    suite.addTest(unittest.makeSuite(FourthExampleTestCase))
    suite.addTest(unittest.makeSuite(FifthExampleTestCase))
    suite.addTest(unittest.makeSuite(SixthExampleTestCase))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite_use_make_suite')