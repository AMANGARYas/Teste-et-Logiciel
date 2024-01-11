
import unittest
import nbPremier
class TestFuncs(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(nbPremier.is_prime(2))      
        self.assertTrue(nbPremier.is_prime(3))      
        self.assertTrue(nbPremier.is_prime(5))      
        self.assertFalse(nbPremier.is_prime(4))     
        self.assertFalse(nbPremier.is_prime(9))     
        self.assertTrue(nbPremier.is_prime(11))         
        self.assertFalse(nbPremier.is_prime(-7))   
        self.assertTrue(nbPremier.is_prime(13))  
        

if __name__ == '__main__':
    unittest.main()

