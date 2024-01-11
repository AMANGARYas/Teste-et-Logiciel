
import unittest
import funcSuiteGeo
class TestFuncs(unittest.TestCase):

    def test_suite_geo(self):
        self.assertTrue(funcSuiteGeo.suite_geo([2, 4, 8, 16, 32]))    
        self.assertTrue(funcSuiteGeo.suite_geo([1, 3, 9, 27, 81]))    
        self.assertTrue(funcSuiteGeo.suite_geo([3, 6, 12, 24, 48]))       
        self.assertFalse(funcSuiteGeo.suite_geo([2, 6, 12, 20, 30]))  
        self.assertTrue(funcSuiteGeo.suite_geo([1, 1, 1, 1, 1]))      
        self.assertTrue(funcSuiteGeo.suite_geo([]))       
        

if __name__ == '__main__':
    unittest.main()

